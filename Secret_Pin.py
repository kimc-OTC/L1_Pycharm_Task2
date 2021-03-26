# set the secret pin as 0456
secret_pin = int('0456')
i = 0000

# run the while loop until the pin has been discovered
while i <= 9999:
    if i == secret_pin:
        print(f"{i:04d}")       # adds a leading zero
        break
    else:
        i += 1
