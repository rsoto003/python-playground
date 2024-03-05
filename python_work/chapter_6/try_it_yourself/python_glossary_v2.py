python_glossary = {
    '.get()': 'can be used on dictionaries. returns message if param is not found.',
    '.title()': 'changes each word in a string to title case, where each word begins with a capital letter.',
    '.strip()': 'removes whitespace on both sides of a string',
    '.removeprefix()': 'removes prefix from a string',
    '.insert()': 'adds a new element at any position in a list.',
    '.pop()': 'the pop method removes the last item in a list.',
    '.remove()': 'will delete an item by specifying the value. helpful when the index is unknown.',
    '.sort()': 'sorts a listalphabetically',
    'sorted()': 'function sorts a list alphabetically temporarily.',
    '.reverse()': 'does not sort alphabetically backwards, just reverses order of the list.'
}


for function, definition in python_glossary.items():
    print(f"\n{function}: {definition}")