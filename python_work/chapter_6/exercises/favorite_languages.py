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

def list_everyones_favorite_languages(list):
    for key, value in list.items():
        print(f"\n {key}'s favorite language is {value}")

list_everyones_favorite_languages(favorite_languages)