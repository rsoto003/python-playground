# try it yourself, page 56
favorite_pizzas = ['pepproni', 'hawaiian', 'margherita']

for pizza in favorite_pizzas:
    print(f"I love {pizza} pizza.")

print('\ni love pizza')

favorite_pizzas.append('veggie')
favorite_pizzas.append('cheese')

print(favorite_pizzas)

# try it yourself - page 65
print(f"The first three items in the list are: {favorite_pizzas[0:3]}")
print(f"The last three items in the list are: {favorite_pizzas[2:]}")
print(f"The middle three items in the list are: {favorite_pizzas[1:4]}")

friend_pizzas = favorite_pizzas[:]

print(favorite_pizzas)
print(friend_pizzas)

favorite_pizzas.append('santa fe')
friend_pizzas.append('chicago')

for pizza in favorite_pizzas:
    print(f"My favorite pizzas are: {pizza}")

for pizza in friend_pizzas:
    print(f"\nMy friend's favorite pizzas are: {pizza}")