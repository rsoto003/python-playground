# Try it yourself on page 84
def calculate_score(color):    
    if color.lower() == 'green':
        print("+5 points!")
    elif color.lower() == 'yellow':
        print("+10 points!")
    elif color.lower() == 'red':
        print("+15 points!")
    else:
        print("you missed your shot!")

calculate_score('red')
calculate_score('magenta')
calculate_score('Yellow')
calculate_score('GREEN')