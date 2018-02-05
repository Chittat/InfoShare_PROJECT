a=3
b=7
c=11


#konwersja typow
z = 4.23
print (type(z),z)
z_int = int(z)
print (type(z_int),z_int )

result = 2^4
print(result)

#print ('before',c)
#c+= 2   #c = c+2
#c-=2
#c*=2
#c/=2
#print ('after',c)

c = c%2 # znak dzielenia z reszta
#print(c)
#zero = 0
#two = 2
#print (two / zero) --- > wywala blad nie dzielenia prez zero


text = 'Ala ma kota'
#eng="tom's house"
#eng2 ='tom\'s house'

#numerowanie stringow
#numerowanie zawsze zaczyna sie od zera, spacje wliczaja sie w numeracje. moze byc od 0 do ... (liczac w prawo) lub od -1 do -..... (liczac w lewo)
letter_a = text[2]
last_char = text[-1]
print(letter_a)
print(last_char)
lenght = len(text) # funkcja len liczy dlugosc znakow w stringu
print (lenght)
#last_char = text[lenght] -- wywala blad string index out of range poniewaz lenght = 11 a string text ma 10 znakow tylko.
print(last_char)

#slices --> wycinanie kawałkow tekstu ze stringow
something = text[3:7] # od 3 do 6 znaku
print(something)
something2=text[-4:-1]#podwawac zawsze od mniejszej do wiekszej!!
print(something2)
steps = text[0:10:2] # od 0 do 10 znaku co drugi znak
print(steps)
print(text[0:15])# nie wyrzuca bledu string index out of range!!
text2=text[::1]
print(text2)
print(text2.upper) # sporo funkcji do modyfikowania outputu

text = '0' + text[1:]
print(text)
text1 = text[:4] + 'M' + text[5:]
print(text1)

