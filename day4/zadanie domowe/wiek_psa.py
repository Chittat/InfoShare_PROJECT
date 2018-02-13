wiek_psa = int(input("Podaj wiek swojego psa: "))

if wiek_psa <= 2:
    ludzki_wiek_psa = str(wiek_psa * 10.5)
    print("Wiek twojego psa to {}".format(ludzki_wiek_psa))

elif wiek_psa > 2:
    ludzki_wiek_psa = str((2 * 10.5) + (wiek_psa - 2) * 4)
    print("Wiek twojego psa to {} lat".format(int(ludzki_wiek_psa)))
    print(type(ludzki_wiek_psa))