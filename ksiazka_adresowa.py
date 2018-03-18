# Person Class to create a Person template
class Person:
    def __init__(self, user_id, name, surname, age, phone=None, email=None):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        c = 'User_id: '  + self.user_id + '\n' + 'Name: ' + self.name + '\n' + 'Surname: ' + self.surname + '\n' + 'Age: ' + self.age + '\n'
        if self.phone is not None:
            c += 'Phone: %s\n' % self.phone
        if self.email is not None:
            c += 'Email address: %s\n' % self.email
        return c


# PhoneBook Class to store Person Data within it
class PhoneBook:
    def __init__(self):
        self.contacts = {}   # dictionary of Person data

# PhoneBook Class function to remove contact details
    def add(self, user_id, name, surname, age, phone=None, email=None):
        p = Person(user_id, name, surname, age, phone, email)
        self.contacts[user_id] = p

# PhoneBook Class function to remove contact details
    def remove(self, user_id):
        if user_id in self.contacts:
            del self.contacts[user_id]
        else:
            print("Contact not available")

# PhoneBook Class function to search for a contact
    def get_contact_detail(self, user_id):
        if user_id in self.contacts:
            return self.contacts.get(user_id)
        else:
            print("Contact not available")

    def __call__(self, user_id):
        return self.contacts[user_id]

    def __str__(self):
        c = ''
        for p in self.contacts:
            c += str(self.contacts[p]) + '\n'
        return c


def add_contact():
    # user_id = input("Enter user_id: ").strip()
    # name = input("Enter contact name: ").strip()
    # surname = input("Enter contact surname: ").strip()
    # age = input("Enter contact age: ").strip()
    # phone = input("Enter contact phone: ").strip()
    # email = input("Enter contact email: ").strip()

    b = PhoneBook()
    #b.add(user_id, name, surname, '33', phone=phone, email=email)
    b.add('Ktos', 'Stefan', 'JakoTako', '33', phone='12345689', email='Stefan.JakoTako@gmail.com')
    b.add('KiwiKiwiKiwi', 'Grazyna ', 'Sprezyna', '22', phone='987654321', email='Grazyna.Sprezyna@gmail.com')
    print(b)

def search_contact():
    b = PhoneBook()
    b.get_contact_detail(user_id='Oko')

def list_all_contacts():
    b = PhoneBook()
    print(b)

def remove_contact():
    user_id = input('Please provide user_id to be deleted: ')
    b = PhoneBook()
    b.remove(user_id)

def start_menu():
    print('Hi! Please choose what would you like to do ? ')
    print("""
Press 1 to check your contacts
Press 2 to enter a new contact
Press 3 to remove existing contacts 
Press 4 to check number of contacts in database
Press 5 to search for a concact
Press 6 to Quit""")

    choice = input().strip()
    if choice == "1":
        list_all_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        remove_contact()
    elif choice == "4":
        calculate_number_of_contacts()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("""Program Closed ! Bye! """)
        exit()
    else:
        print("Wrong option! Choose Again!")
        print()

while True:
    start_menu()