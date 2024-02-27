# Try it yourself on page 84

def stage_of_life(age):
    if age < 2:
        print("you're just a baby!")
    elif age >= 2 and age < 4:
        print("you're a toddler!")
    elif age >= 4 and age < 13:
        print("you're just a kid!")
    elif age >= 13 and age < 20:
        print("you're a teenager!")
    elif age >= 20 and age < 65:
        print("you're an adult!")
    else:
        print("you are an elder.")

stage_of_life(1)
stage_of_life(3)
stage_of_life(9)
stage_of_life(17)
stage_of_life(45)
stage_of_life(99)