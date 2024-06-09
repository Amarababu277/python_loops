# the enumerate() function is used with the for loop to iterate over an iterable while also
# keeping track of the index of each item.

list1 = ['Amara', 'Snehith', 'Teja', 'rakesh', 'Akshay']

for count, elements in enumerate(list1):
    print(elements, count)