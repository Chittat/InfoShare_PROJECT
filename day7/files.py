import os

FILENAME = 'dlugosc_pliku.txt'

file_size=os.path.getsize(FILENAME)
print(f'Rozmiar pliku: {file_size}')

with open(FILENAME) as plik:
    for char in plik:
        print(plik)