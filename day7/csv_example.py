#imie = input('Podaj Imie do zapisu: ').strip()
#nazwisko =input('Podaj Nazwisko do zapisu: ').strip()
#wiek = input('Podaj wiek: ').strip()


#FORMAT ='{imie}, {nazwisko},{wiek}\n'
#with open('osoby', 'a') as plik:
#    plik.write (FORMAT.format(imie = imie, nazwisko = nazwisko, wiek = wiek))
#   print(plik)

import csv

with open('osoby') as plik:
    reader = csv.reader(plik)
    for line in reader:

        print(line)