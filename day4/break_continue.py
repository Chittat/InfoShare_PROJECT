counter = 0
value = input('Podaj Liczbe: ')
value = int(value)

#@TODO: wyswietl na ekran wartosc counter
#@TODO: wyswietl tylko jesli counter jest nieparzysty
while counter < value:
    if counter % 2:
        print(counter)
        counter += 1
    elif value > 1000:
        break
    else:
        counter += 1
        continue
print('bye')