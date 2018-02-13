data=input('Podaj dowolna licze lub litere: ')

while not data.isalpha() and not data.isdigit():
    print('Podales zle dane, podaj poprawne: ')
    data = input('Podaj dowolna licze lub litere: ')
if data.isdigit():
    print('podales liczbe')
elif data.isalpha():
    print ('podales litere')
print('bye')

