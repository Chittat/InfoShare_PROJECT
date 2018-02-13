#@TODO: pobierz od uzytkownika dowolna liczbe lub znak
#@TODO: sprawdz czy podane dane to liczba czy litera
#@TODO: wyswietl stosowny komunikat. Np: "wprowadziles liczbe"
data=input('Podaj dowolna licze lub litere: ')
#data.isalpha()
#data.isdigit()
if data.isdigit():
    print('podales liczbe')
    print('bye')
elif data.isalpha():
    print ('podales litere')
    print('bye')
else:
    print('HELP!')

