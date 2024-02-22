# This file is for containing a list of all functions/methods that are introduced while completing the book.

''' 
    .title() - method
    .title() is a method that performs an action on a piece of data. in this case, 
    the action being performed is changing each word in the string to title case, where each word begins with a capital letter 
'''
favorite_basketball_player = 'lebron james'

print(favorite_basketball_player.title())

#########################################################################################################################################

'''
    stripping whitespace - can be performed by 3 different methods:
    .rstrip() - removes whitespace at the right side of the string
    .lstrip() - removes whitespace at the left side of the string
    .strip() - removes whitespace on both sides of the string
'''
whitespace_string = '   lebron james    '

print(whitespace_string.rstrip())
print(whitespace_string.lstrip())
print(whitespace_string.strip())

#########################################################################################################################################

'''
    removing prefixes and suffixes
    .removeprefix() - removes a prefix from string. example would be removing the www. or https:// from a URL
    .removesuffix() - removes suffix from a string. example would be removing a .com from a URL
'''
url = 'www.google.com'
email = 'test@gmail.com'

print(url.removeprefix('www.'))
print(email.removesuffix('.com'))

#########################################################################################################################################

'''
    .append() - adds a new item to the end of a list
'''
append_list = ['one', 'two']

append_list.append('three')
print(append_list)

#########################################################################################################################################

'''
    .insert() - adds a new elemnt at any position in a list.
    this must be done by specifying which position in the list via the index
'''
insert_list = ['one', 'three']

insert_list.insert(1, 'two')
print(insert_list)

#########################################################################################################################################

'''
    del statement - removes an item from the list via specifying the index
'''

del_list = ['one', 'one-million', 'three']

del del_list[1]
print(del_list)

#########################################################################################################################################

'''
    .pop() - the pop method removes the last item in a list.
    * the catch here is you are still able to work with that item after removing it
    * additionally, if you want to remove a specific index, pass that index in.
'''
pop_list = ['1', '2', '3']
popped = pop_list.pop()

print(pop_list)
print(popped)

#########################################################################################################################################

'''
    .remove() will delete an item by specifying the value. helpful when the index is unknown.
    * this method only deletes the first occurrence of the value that is specified.
'''

remove_list = ['1', '2', 'september', '3']

remove_list.remove('september')
print(remove_list)

#########################################################################################################################################

'''
    .sort() - sorts a listalphabetically
    * important to note - .sort() changes the order of the list permanently. you can never revert to the previous order.
    * can pass in "reverse=True to sort reverse-alphabetical order
'''

sort_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

sort_list.sort()
print(sort_list)

sort_list.sort(reverse=True)
print(sort_list)

#########################################################################################################################################

'''
    sorted() function sorts a list alphabetically temporarily.
    * this is helpful when the original order of a list needs to be maintained.
'''
sorted_list = ['bmw', 'audi', 'toyota', 'suburu']

print(sorted_list)
print(sorted(sorted_list))
print(sorted_list)

#########################################################################################################################################

'''
    .reverse() does not sort alphabetically backwards, just reverses order of the list.
'''
reverse_list = ['bmw', 'audi', 'toyota', 'suburu']

print(reverse_list)
reverse_list.reverse()
print(reverse_list)

#########################################################################################################################################

'''
    len() - length of a list
'''

print(len(reverse_list))

#########################################################################################################################################

'''
    range() - generates a series of numbers between a range.
    first two arguments are simply the range in which you wish your numbers to be between.
    the third argument is the step size in which numbers are generated.
'''

for value in range(1,10):
    print(value)

############################################################################################################################
    
'''
    list() - converts a set of numbers into a list.
'''
even_numbers = list(range(2, 11, 2))
print(even_numbers)

############################################################################################################################

'''
    min()
    max()
    sum()

    do exactly as you'd think they'd do.
'''

############################################################################################################################

'''
    list comprehensions:
        combines the for loop and the creation of new elements into one line, and automatically appends each new element.
'''
squares_v2 = [value**2 for value in range(1, 11)]
print(squares_v2)

############################################################################################################################

'''
    SLICING A LIST:
        same idea as the range() function syntax.
'''
players = ['ryan', 'kobe', 'mookie', 'freddie', 'shaq']
print(players[0:4])
print(players[:2])
print(players[3:])

############################################################################################################################
'''
    TUPLES:
        immutable: value that cannot change.
        immutable list = list of values that cannot change, aka tuple
        same syntax as lists, but instead of brackets, use paranthesis
'''