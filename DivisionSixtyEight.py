# Testing two numbers for division

while True:
    try:
        test1 = int(input("Enter the first number:"))
    except ValueError:
        print("Ooops, not a valid one")
        continue
    try:
        test2 = int(input(" Enter the second number:"))
    except ValueError:
        print("Ooops, not valid")
        continue
    if test1 % test2 == 0 or test2 % test1 == 0:
        print(" they are divisible and value is 1")
        break
    else:
        print("not divisible, value is 0")
        break
