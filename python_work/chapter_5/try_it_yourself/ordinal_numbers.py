# try it yourself, page 88
numbers = [1,2,3,4,5,6,7,8,9]
empty_list = []

def ordinal_numbers(numbers_list):
    if numbers_list:
        for number in numbers_list:
            if number == 1:
                print(f"{number}st")
            elif number == 2:
                print(f"{number}nd")
            elif number == 3:
                print(f"{number}rd")
            else:
                print(f"{number}th")
    else:
        print("don't waste my time ----- add some numbers")

ordinal_numbers(numbers)
ordinal_numbers(empty_list)