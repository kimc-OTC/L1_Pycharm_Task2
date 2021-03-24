secret_pin = int('0456')
i = 0000
while i <= 9999:
    if i == secret_pin:
        print(f"{i:04d}")
        break
    else:
        i += 1
