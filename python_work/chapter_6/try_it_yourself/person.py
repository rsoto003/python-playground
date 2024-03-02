person_i_know = {
    'first_name': 'LeBron',
    'last_name': 'James',
    'age': 39,
    'city': 'Los Angeles'
}

def display_personal_info(personal_info):
    print(f"Full Name: {personal_info['first_name']} {personal_info['last_name']}")
    print(f"Age: {personal_info['age']}")
    print(f"City of current residence: {personal_info['city']}")

display_personal_info(person_i_know)