from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

code = """
s = "malayalam"  # string

i,j = 0, len(s) - 1  # two pointers

is_palindrome = True  # assume palindrome
while i < j:
    if s[i] != s[j]:  # mismatch found
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes") 
else:
    print("No")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=200, chunk_overlap=0
)


chunks = splitter.split_text(code)

print(len(chunks))
print("---------------------")
print(chunks[0])
print("---------------------")
print(chunks[1])
print("---------------------")
print(chunks[2])
