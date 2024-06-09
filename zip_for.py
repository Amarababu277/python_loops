# zip() function iterates over two lists in parallel. The for loop assign
# the corresponding elements of both lists in every each iteration.

fruits = ['apple', 'orange', 'amla']

colors = ['red', 'orange', 'green']

for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)