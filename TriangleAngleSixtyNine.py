# Figuring third triangle angle

while True:
    try:
        angle1 = float(input("Enter first angle:"))
    except ValueError:
        print("Ախպեր, սխալ է")
        continue
    try:
        angle2 = float(input("Enter second angle"))
    except ValueError:
        print("Непорядок дружок, некорректный ввод, так не пойдет")
        break
    if (angle1 > 0 and angle2 > 0) and (angle1 + angle2 < 180):
        print(f" The third angle is equal to: { 180 -angle1 - angle2}")
        break
    else:
        print(" These are not valid angles for triangle")
        break

