h = input("Podaj wysokosc piramidy: ")
wysokosc = int(h)

for i in range(wysokosc):
	print (" "*(wysokosc-1*i)+("#")+("#"*(2*i)))