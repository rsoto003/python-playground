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
    for name, language in list.items():
        if language == 'python':
            print(f"wow, {name.title()}, my favorite language is {language.title()} too!")
        else:
            print(f"oh, {name.title()}, don't worry, i'm sure {language.title()} is great as well.")

list_everyones_favorite_languages(favorite_languages)