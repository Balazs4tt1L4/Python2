szam = int(input("Adj meg egy egész számot: "))

if szam % 3 == 0 and szam % 5 == 0:
    print("A szám 3-mal és 5-tel is osztható.")
elif szam % 3 == 0:
    print("A szám osztható 3-mal.")
elif szam % 5 == 0:
    print("A szám osztható 5-tel.")
else:
    print("Egyikkel sem osztható")