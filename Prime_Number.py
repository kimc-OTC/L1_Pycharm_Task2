user_number = int(input("Type in a number."))
i = 2
if user_number > 1:
    while (user_number % i) == 0:
        print("{} is not a prime number.".format(user_number))
        user_number = int(input("Type in another number."))
    else:
        print("{} is a prime number.".format(user_number))
else:
    print("{} is not a prime number.".format(user_number))


