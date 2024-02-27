# example on page 87:
available_toppings = ['mushrooms', 'olives' 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding requested topping: {requested_topping}")
    else:
        print(f"i am sorry, we don't have {requested_topping}")

print('\nfinished making your pizza!')