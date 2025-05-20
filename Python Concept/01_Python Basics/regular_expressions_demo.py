"""
Regular Expressions in Python
-----------------------------
Regular expressions (regex) are a powerful tool in Python for searching, matching, and manipulating text.
The `re` module provides support for regex operations.

Common Use Cases of Regex:
--------------------------
1. Validating input (e.g. email, phone number, passwords)
2. Searching for specific patterns in text
3. Extracting data from unstructured text
4. Replacing or splitting strings based on patterns
"""

import re

def demonstrate_regex():
    print("==== REGULAR EXPRESSIONS DEMO ====\n")

    sample_text = """
    Hello, my name is Aslam. My email is aslam123@gmail.com.
    You can also contact me at work_email@company.org or visit https://myportfolio.io.
    My phone number is +880-176-000-1234.
    """

    # 1. Extract all email addresses
    email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    emails = re.findall(email_pattern, sample_text)
    print("1. Found Emails:")
    print(emails)

    # 2. Extract all URLs
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, sample_text)
    print("\n2. Found URLs:")
    print(urls)

    # 3. Extract phone number
    phone_pattern = r'\+880-\d{3}-\d{3}-\d{4}'
    phones = re.findall(phone_pattern, sample_text)
    print("\n3. Found Phone Numbers:")
    print(phones)

    # 4. Replace all emails with [EMAIL]
    masked_text = re.sub(email_pattern, '[EMAIL]', sample_text)
    print("\n4. Masked Emails in Text:")
    print(masked_text.strip())

    # 5. Search if a name exists
    match = re.search(r'\bAslam\b', sample_text)
    if match:
        print("\n5. Name 'Aslam' found at position:", match.start())

    # 6. Split sentence by space or newline
    words = re.split(r'\s+', sample_text)
    print("\n6. Split into Words (first 10):")
    print(words[:10])

if __name__ == "__main__":
    demonstrate_regex()
