# asks the user to pick a number
user_number = int(input("Type in a number."))

# set i as 2 because prime number is only divisible by 1 and itself
i = 2

# tells the user if the number is prime or not. If not, keep on asking the user for another number
while user_number > 1:
    if user_number == 2:
        print("{} is a prime number.".format(user_number))
        break
    elif (user_number % i) == 0:
        print("{} is not a prime number.".format(user_number))
        user_number = int(input("Type in another number."))
    else:
        print("{} is a prime number.".format(user_number))
        break
else:
    print("{} is not a prime number.".format(user_number))


