# try it yourself exercise on page 41
guest_list = ['kobe bryant', 'nipsey hussle', 'lebron james', 'shohei ohtani', 'caleb williams', 'denzel washington']
guest_who_cannot_attend_index = guest_list.index('caleb williams')
guest_to_replace_aforementioned_guest = 'reggie bush'

for guest in guest_list:
    print(f"\tHi {guest.title()}, would you like to attend my dinner party?")

# initial guest list
print(guest_list)

print(f"Unfortunately, {guest_list[guest_who_cannot_attend_index].title()} is no longer able to attend.\n{guest_to_replace_aforementioned_guest.title()} will be replacing that guest.")

guest_list.pop(guest_who_cannot_attend_index)
guest_list.insert(guest_who_cannot_attend_index, guest_to_replace_aforementioned_guest)

print(guest_list)

for guest in guest_list:
    print(f"\tHi, {guest.title()}, slight update to the dinner invite. Now starting at 6PM.")

print('\nHello, we now have additional tables. Will be sending out more invites.')

guest_list.insert(0, 'dua lipa')
guest_list.insert(3, 'Drake')
guest_list.append('Rocky')

for guest in guest_list:
    print(f"\tHi, {guest.title()}, this is hopefully the last batches of invites. Apologies.")

# try it yourself 3-7, page 42
print('As per my last email - that no one responded to - we no longer are going to get our tables in time. The list will be downsized. That is all.')

guest_list_length = len(guest_list)
while guest_list_length > 2:
    guest_removed = guest_list.pop()
    guest_list_length-=1
    print(f"Apologies, {guest_removed.title()} - you are no longer invited. Sorry lol")
    print(f"\tGuest List Length: {guest_list_length}")


for remaining_guest in guest_list:
    print(f"Dear: {remaining_guest.title()} - you are still invited if you want to join. Should still be fun. Let me know, asap. Thanks.")

del guest_list[0]
del guest_list[0]

print(guest_list)
