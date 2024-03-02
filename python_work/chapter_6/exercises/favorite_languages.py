favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

ryans_fav_language = favorite_languages.get('ryan', 'Sorry, that user does not exist yet.')
print(ryans_fav_language)

favorite_languages['ryan'] = 'typescript'
ryans_fav_language = favorite_languages.get('ryan', 'Sorry, that user does not exist yet.')
print(ryans_fav_language)