# try it yourself exercise on page 41
guest_list = ['kobe bryant', 'nipsey hussle', 'lebron james', 'shohei ohtani', 'caleb williams', 'denzel washington']
guest_who_cannot_attend = guest_list.index('caleb williams')
guest_to_replace_aforementioned_guest = 'reggie bush'

for guest in guest_list:
    print(f"Hi {guest.title()}, would you like to attend my dinner party?")

# initial guest list
print(guest_list)

print(f"Unfortunately, {guest_list[guest_who_cannot_attend].title()} is no longer able to attend.\n{guest_to_replace_aforementioned_guest.title()} will be replacing that guest.")

guest_list.pop(guest_who_cannot_attend)
guest_list.insert(guest_who_cannot_attend, guest_to_replace_aforementioned_guest)

print(guest_list)

for guest in guest_list:
    print(f"Hi, {guest.title()}, slight update to the dinner invite. Now starting at 6PM.")