# continue statement return the control to the beginning of the loop.

# prints all letters except 'e' and 's'

for letter in "geeksforgeeks":

    if letter == 'e' or letter == 's':
        continue
    print('Current letter :', letter)

# break statement brings control out of the loop.

for letter in 'geeksforgeeks':

    if letter == 'r':
        break
    print('Current letter :', letter)