import sys
import csv
import pandas as pd


with open('adress_book.csv','w', newline='') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['user_id','name', 'surname', 'age', 'phone_number'])
    newFile.close()

#Main menu to start the application and choose the option.
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

#Function to add a new contact details into the database
def add_contact():
    print()
    contact_id = input("Enter contact_id: ").strip()
    name = input("Enter contact name: ").strip()
    while not name.isalpha():
        name = str(input('Name cant be a number! Please enter a valid name: '))
    surname = input("Enter contact surnamename: ").strip()
    while not surname.isalpha():
        surname = str(input('Surname cant be a number! Please enter a valid surname: '))
    phone_number = input("Enter contact phone_number: ").strip()
    age = input("Enter contact age: ").strip()
    while not age.isdigit():
        age = str(input('Age must be a number! Please enter a valid age: '))

    with open('adress_book.csv', 'a', newline='') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([contact_id, name, surname, age, phone_number])
        newFile.close()
    print()
    print("User {} has been added to the adress book".format(contact_id))
    print()

#Function to remove contact from the adress book
def remove_contact():
    print()
    contact_id = input("Enter contact_id to be deleted: ")
    df = pd.read_csv('adress_book.csv', index_col='user_id')
    df.drop(contact_id, inplace=True)
    df.to_csv('adress_book.csv')
    print("contact removed.")
    print()

#Function to calculate number of contacts in the adress book
def calculate_number_of_contacts():
    print()
    print('Your number of contacts is {}'.format(len(open('adress_book.csv').readlines())-1))
    print()

#Function to search for the contact in the adress book
def search_contact():
    print()
    user_id = input("Please provide user_id : ")
    with open('adress_book.csv', 'r') as myfile:
        reader = csv.DictReader(myfile)
        for row in reader:
            if row['user_id'] == user_id:
                print("User {} has been found in adress book".format(user_id))
                print(row['user_id'], row['name'], row['surname'], row['age'], row['phone_number'])
                break
        else:
            print('No contacts found')
    print()

#Function to list all contacts from the adress book
def list_all_contacts():
    print()
    print("Twoja lista kontaktow:")
    with open('adress_book.csv', 'r') as userFile:
        userFileReader = csv.DictReader(userFile)
        for row in userFileReader:
            print(row['user_id'], row['name'], row['surname'], row['age'], row['phone_number'])
    print()

while True:
    start_menu()