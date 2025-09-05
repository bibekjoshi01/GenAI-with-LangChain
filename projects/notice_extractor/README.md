# Application the Extract Notices from website and Posts in Website

### Simple Pipeline

1. **Scrape Websites**

   - Use `requests + BeautifulSoup` (or `playwright` for JS sites).
   - Save **raw HTML + plain text**.

2. **Preprocess**

   - Remove headers/footers/menus.
   - Keep main text sections (`<main>`, `<article>`, `<table>`).
   - Clean whitespace, scripts, ads.

3. **Chunking**

   - Split long text into smaller chunks.

4. **LLM Extraction**

   - Feed each chunk into an LLM with a **strict JSON schema** (title, date, description, source_url).
   - Use `JsonOutputParser` + `OutputFixingParser`.

5. **Post-Processing**

   - Validate JSON (check date format, empty fields).
   - Deduplicate repeated notices.
   - Normalize text (trim, lowercase, fix dates).

6. **Storage**

   - Store both **raw content** + **structured JSON** in DB (Postgres/Mongo) or files.
   - Add metadata: source site, timestamp, language.

7. **Usage**

   - Expose via API or dashboard.
   - Optionally index with a vector DB for semantic search.

---

**Scrape → Clean → Chunk → LLM Extract → Validate → Store → Use.**
