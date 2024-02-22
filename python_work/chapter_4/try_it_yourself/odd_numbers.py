odd_numbers = [value for value in range(1, 20, 2)]

for num in odd_numbers:
    print(num)

print("\nThis was completed by list comprehension.\n")

odd_numbers_v2 = list(range(1,20,2))

for num in odd_numbers_v2:
    print(num)

print("\nThis was done by a simple list function combined with the range function.\n")
