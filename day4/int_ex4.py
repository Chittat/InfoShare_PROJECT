#@TODO;podaj dane ktora sa liczba
#@TODO: liczba jest rozna od zera

data=input('Podaj dowolna liczbe rozna od zera: ')

while not data.isdigit() or data=='0':
    print('Podales zle dane, podaj poprawne: ')
    data = input('Podaj dowolna liczbe rozna od zera: ')

print('bye')
