alien_0 = { 'color': 'green', 'points': 5}

alien_1 = { 'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# move alien to the right
# determine HOW FAR by the alien's current speed

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# the new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position: {alien_1['x_position']}")