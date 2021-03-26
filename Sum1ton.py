# ask the user to pick a number
n = int(input("Type in a number"))
sum_numbers = 0

# print the sum of the numbers from 1 to n
for i in range(1, n + 1):
    sum_numbers = sum_numbers + i
print(sum_numbers)

# or
# print((1 + n) * n/2)


