from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
What is a cloud database? An in-depth cloud DBMS guide
Which also includes:
Should you run your database on premises or in the cloud?
Cloud DBA: How cloud changes database administrator's role
On-premises vs. cloud data warehouses: Pros and cons
Within larger organizations, DBA responsibilities typically are split into separate types of roles. Beyond general-purpose, the primary roles include system DBA, database architect, database analyst, application DBA, task-oriented DBA, performance analyst, data warehouse administrator and cloud DBA.

System DBA
This role focuses on technical, rather than business, issues. The system DBA is knowledgeable in the arcane technical details of how the database is installed, configured and modified. Typical tasks center on the physical installation and performance of the DBMS software and can include the following:

Installing new software versions and applying fixes.
Setting and tuning system parameters.
Tuning the operating system, network and transaction processors to work with the DBMS.
Ensuring appropriate storage and memory are available for the DBMS.
System DBAs are rarely involved with the actual database and application set up. They might get involved in application tuning when operating system parameters or complex DBMS parameters need to be altered.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)
print("-------------------------")
print(chunks[0])