# try it yourself, page 88
current_users = ['ryansoto', 'ADMIN', 'rocky123', 'marcopolo', 'lebronjames']

new_users = ['kobebryant', 'darvinham123', 'RYANSOTO', 'mookiebetts', 'dodgersfan123']

def check_valid_user_name(new_usernames, current_usernames):
    for user in new_usernames:
        if user.lower() in current_usernames:
            print(f"apologies, but {user} is already taken. identity theft is not a joke, jim!")
        else:
            print("awesome, that username is available.")

check_valid_user_name(new_users, current_users)