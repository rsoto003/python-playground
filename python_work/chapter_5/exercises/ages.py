age_1 = 28
age_2 = 30

if age_1 >= 30 and age_2 >= 30:
    print('this condition is true')
else:
    print('this is not true')

child_age = 8
teenager_age = 13
young_adult_age = 18
legal_adult_age = 21
slightly_mature_adult_age = 30

def verify_drinking_age(age):
    print(f'inputted age: {age}')
    if age >= 21:
        print('you are able to consume alcohol, please drink responsibly.\n')
    else:
        print('you are not legal. you better grab a soda instead.\n')

verify_drinking_age(child_age)
verify_drinking_age(teenager_age)
verify_drinking_age(young_adult_age)
verify_drinking_age(legal_adult_age)
verify_drinking_age(slightly_mature_adult_age)