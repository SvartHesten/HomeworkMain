# sum of n + nn + nnn where n is positive int

while True:
    number_string = input("Enter the positive integer value")
    try:
        number = int(number_string)

    except ValueError:
        print(" O o ops, not a valid number")
        continue
    if number > 0:
        number1 = number * (10 ** len(number_string)) + number
        number2 = number * (100 ** len(number_string)) + number *(10 ** len(number_string)) + number
        print(f" Result equal to: {number + number1 + number2 }")
        break
    else:
        print(" next time enter a positive number")
        break
