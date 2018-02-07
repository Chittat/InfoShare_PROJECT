#digit = input('podaj liczbe: ')
#zamiana str na int
#digit = int(digit)

#@TODO:
#if is even
#    print ('liczba jest parzysta')
#@TODO: w przeciwnym wypadku wyswietl liczba nie jest parzysta

digit = input('Podaj liczbe: ')
digit = int(digit)
check = (digit % 2)
if check == 0:
    print ('licza jest parzysta')
else:
    print ('liczba jest nieparzysta')

