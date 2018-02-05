# funkcja replace
text3 = "ala ma kota kot zjada ale"
old = 'kot'
new ='pies'
count = 1
replaced=text3.replace(old,new,count) # count mowi zeby tylko 1 wystapienie slowa kot zastapic. mozna uzyc liczb zamiat funkcji
print(text3,id(text3))
print(replaced,id(replaced))