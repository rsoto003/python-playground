# my solution for printing a range where each number in range is squared
for num in range(1,20):
    square_root = num * num
    print(square_root)

# book solution for generating a list of squared numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# list comprehension example:
squares_v2 = [value**2 for value in range(1, 11)]
print(squares_v2)