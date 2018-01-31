name = input('Podaj swoje imie: ')
print(name)
message = 'Twoje imie to: '
print('Twoje imie to: ', name)   #zle podejscie do wyswietlania
print(message, name)            #dobre podejscie
#\n new line

#najlepsze podejscie
age = 999
message = f'Twoje imie to: {name} {age}' #formatted string
print(message)