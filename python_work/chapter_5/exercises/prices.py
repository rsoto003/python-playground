def check_prices(age):
    print(f"\ninputted age: {age}")
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    elif age < 16:
        price = 20
    elif age < 18:
        price = 50
    else:
        price = 1000
    print(f"Your admission price is ${price}")


check_prices(3)
check_prices(2)
check_prices(13)
check_prices(25)