my_list = list(range(0,11,2))
print(my_list)

text ="ala ma kota"
something = list(text)
print(something)


for idx, element in enumerate(list1):
    print(idx, element)

    for value in enumerate(something):
        print(value)

my_list.append(13)
print(my_list)

my_list.reverse() # IN PLACE

my_list2 = reversed(my_list)
reversed(my_list)

