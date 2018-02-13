liczba = int(input("Podaj dowolna liczbe: "))

print("Tabliczka mnozenia liczby", liczba)
for x in range(1,11):
    print(liczba, "x", x, "=", liczba*x)