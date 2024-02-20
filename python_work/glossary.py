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
'''
pop_list = ['1', '2', '3']
popped = pop_list.pop()

print(pop_list)
print(popped)