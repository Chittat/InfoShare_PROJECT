a = 0
b = 2.34
text = 'abc'

if b > a:
    print('b>a')

if b<a:
    print('b<a')


if b>a:
    print("b>a")
elif b==a:
    print("b=2")
else:
    print("b<a")

result = a> b
print (type(result), result)

if text:
    print('teskt is not empty')

x=1
y=2
z=3
if x<y<z:
    print('o kurwa! jest wieksze!')

#@ TODO: if 'a'< 'h' < 'z' sprawdzic jak jest to sortowane

something = 'abc'
another = 'xyz'

if something == 'abc' and another =='xyz':
        print('strings are the same')

is_rest_equal_to_zero = 4 % 2
if not is_rest_equal_to_zero:
    print('the numer is even')

name = 'Jan'
lastnme ='kowalski'

if name =="Jan" or lastname=="kowalski":
    print('siema!')