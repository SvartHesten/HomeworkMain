# moving last digit of integer to front
# if last digit zero do not move

while True:
    num_str = input(" Enter the number")
    try:
        num = int(num_str)
    except ValueError:
        print(" Ooops , invalid data")
        continue
    if len(num_str) == 1 or num_str[len(num_str) - 1] == "0":
        print(f" and the modified number equals {num_str}")
        break
    else:
        first_str = num_str[len(num_str) - 1]
        for i in range(len(num_str) - 1):
            first_str = first_str + num_str[i]
        print(first_str)
    break

