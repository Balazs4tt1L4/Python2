szamok = []

for i in range(7):
    het_szam = int(input("Adj meg egy számot: "))
    szamok.append(het_szam)

negativ = 0
pozitiv = 0
for szam in szamok:
    if szam < 0:
        negativ += 1
print(f"{negativ}db negatív szám van.")

for szam in szamok:
    if szam > 0:
        pozitiv += 1
print(f"{pozitiv}db pozitív szám van.")

print(f"A legkisebb szám a listában a(z): {min(szamok)}")
print(f"A legnagyobb szám a listában a(z): {max(szamok)}")
