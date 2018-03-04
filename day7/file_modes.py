#constant_value
FILENAME = 'dlugosc_pliku.txt'

print('tryb do odczytu')
with open(FILENAME, 'r') as plik:
    cursor = plik.tell()
    print('przed odczytem', cursor)
    print(plik.read())
    print('po odczycie')
    cursor = plik.tell()
    print(cursor)

##print('tryb do zapisu')
#with open (FILENAME, 'w') as plik:
#    print(plik.read())

print('tryb dopisywania')
with open(FILENAME,'a') as plik:
    plik.write('ala ma kota')