name = 'Ala'

def hellp(username):
    '''
    Returns uppercased username.
    :param username:
    :return:
    '''
    name = username.upper()
    return(name)

data = input('podaj imie')
uppercased = hellp(data)
print(uppercased)
print(name
      )