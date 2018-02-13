start = int(input("podaj start: "))
stop = int(input("podaj stop: "))
krok = int(input("podaj krok: "))
liczby_parzyste = 0
liczby_nieparzyste = 0

for x in range(start, stop + 1, krok):
    if x%2 == 0:
        liczby_parzyste = liczby_parzyste +1
    else:
        liczby_nieparzyste = liczby_nieparzyste + 1

print("ilosc liczb parzystych w zbiorze to {}".format(liczby_parzyste))
print("ilosc liczb nieparzystych w zbiorze to {}".format(liczby_nieparzyste))
