#def infinite_argument(*args):   #* oznacza niezdefiniowana liczbe argumentow pozycyjnych
#    print(args)

#infinite_argument(1,2,3,4,5)

#def function(*args):
#    return(sum(args))

def improved_sum_with_return(*args):
    '''
    Sum any number
    :param args:
    :return:
    '''
    pass
    value = sum(args)
    return value

values_to_sum =[1, 2, 10, 15]
result = improved_sum_with_return(*values_to_sum)
print(result)

def compare(a,b):
    return a> b

print(compare(1,2))
print(compare(4,2))