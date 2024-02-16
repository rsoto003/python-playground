github_url = 'https://github.com/rsoto003'

email = 'test_user@gmail.com'

print(f'Github URL, before prefix removal: {github_url}')

print(f'Github username, after removing url data: {github_url.removeprefix('https://github.com/')}')

print(f'Email: {email}')

print(f'Email after removing domain: {email.removesuffix('@gmail.com')}')