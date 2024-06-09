# This code uses nested for loops to iterate over two two ranges of numbers (0 to 3 incl)
# and prints the value of i and j for each combination of the two loops.
# The inner loop is executes for each value of i in the outer loop.
# the output of the code will print the numbers from 1 to 3 three times,
# as each value of the i is combined with each value of j.

for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)