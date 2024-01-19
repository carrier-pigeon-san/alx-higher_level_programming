#!/ust/bin/python3
"""
read_file() function module
"""


def read_file(filename=""):
    """reads a text file and prints it out to stdout"""
    with open(filename, 'r', encoding="utf-8") as doc:
        content = doc.read()
        print(content, end="")
