import logging
from datetime import datetime
from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

from utils import save_json, clean_body_html
from websites import websites

MAX_RETRIES = 3
PARALLEL_PAGES = 4

# Setup logging
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


async def scrape_single_website(sem, website):
    async with sem:  # limit concurrency
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=True)
            context = await browser.new_context(ignore_https_errors=True)
            page = await context.new_page()

            url = website["url"]
            logging.info(f"Scraping {url} ...")
            success = False

            for attempt in range(MAX_RETRIES):
                try:
                    await page.goto(url, timeout=30000, wait_until="networkidle")
                    content = await page.content()
                    body_html = str(BeautifulSoup(content, "html.parser").body or "")
                    clean_html = clean_body_html(body_html)

                    data = {
                        "name": website["name"],
                        "category": website["category"],
                        "url": url,
                        "scrape_time": datetime.now().isoformat(),
                        "status": "success",
                        "content": clean_html,
                    }
                    save_json(website["name"], data)
                    success = True
                    break
                except PlaywrightTimeout as e:
                    logging.warning(f"Timeout while loading {url}: {e}")
                except Exception as e:
                    logging.error(f"Error scraping {url}: {e}")

            if not success:
                logging.error(f"Failed to scrape {url} after {MAX_RETRIES} attempts")
                save_json(
                    website["name"],
                    {
                        "name": website["name"],
                        "category": website["category"],
                        "url": url,
                        "scrape_time": datetime.now().isoformat(),
                        "status": "failed",
                        "content": "",
                    },
                )
            await browser.close()


async def scrap_notices(websites):
    sem = asyncio.Semaphore(PARALLEL_PAGES)
    tasks = [scrape_single_website(sem, w) for w in websites]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(scrap_notices(websites))

    print("Scraping finished. Check scraper.log and scraped_notices folder.")
