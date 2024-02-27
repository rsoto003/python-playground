# try it yourself, page 88
usernames = ['ryansoto', 'ADMIN', 'rocky123', 'marcopolo', 'lebronjames']
empty_users = []

def welcome_new_users(users):
    if users:
        for user in usernames:
            if user.lower() == 'admin':
                print(f"Hello, {user}. Here is your daily status report.")
            else:
                print(f"Hello, {user} - thank you for logging in again.")
    else:
        print("\nwhere did our users go! we need to recover our users.")


welcome_new_users(usernames)
welcome_new_users(empty_users)