python_glossary = {
    '.get()': 'can be used on dictionaries. returns message if param is not found.',
    '.title()': 'changes each word in a string to title case, where each word begins with a capital letter.',
    '.strip()': 'removes whitespace on both sides of a string',
    '.removeprefix()': 'removes prefix from a string',
    '.insert()': 'adds a new element at any position in a list.'
}

def display_glossary(glossary):
    for item in glossary:
        print(f"{item}: {glossary[item]}")

display_glossary(python_glossary)