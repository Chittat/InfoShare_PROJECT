my_list = list(range(10))
my_list2 = reversed(my_list)

if my_list == my_list2:
    print("my_list jest taka sama jak my_list2")
else:
    print("my_list nie jest taka sama jak my_list2")

import copy

my_list2 = copy.deepcopy(my_list)
my_list = my_list.reverse()

if my_list == my_list2:
    print("my_list jest taka sama jak my_list2")
else:
    print("my_list nie jest taka sama jak my_list2")

print(my_list, my_list2)

