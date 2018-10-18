import math

def equation():
    a = float(input("Palun sisesta esimene võrrand"))
    b = float(input("Palun sisesta teine võrrand"))
    c = float(input("Palun sisesta kolmas võrrand"))

    discRoot = math.sqrt((b * b) - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("Vastused on, X1:", dp % root1,"X2:", dp % root2)

if __name__ == '__main__':
    equation()
else:
    pass