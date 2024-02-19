# try it yourself page 45
dream_travel_locations = ['New York City', 'Paris', 'Tokyo', 'Bora Bora', 'Vancouver']

print("\nOriginal List")
print(dream_travel_locations)

print("\nList, sorted alphabetically")
print(sorted(dream_travel_locations))

print("\nOriginal List again just to confirm:")
print(dream_travel_locations)

print("\nList, sorted in reverse, alphabetically")
print(sorted(dream_travel_locations, reverse=True))

print("\nOriginal List again just to confirm:")
print(dream_travel_locations)

print("\nReversing the list")
dream_travel_locations.reverse()
print(dream_travel_locations)

print("\nReverting the reverse")
dream_travel_locations.reverse()
print(dream_travel_locations)

print("\nSorting in alphabetical order, permanently")
dream_travel_locations.sort()
print(dream_travel_locations)

print("\nSorting in reverse-alphabetical order, permanently")
dream_travel_locations.sort(reverse=True)
print(dream_travel_locations)