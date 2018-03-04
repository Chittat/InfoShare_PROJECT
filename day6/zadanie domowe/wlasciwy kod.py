import sys
import csv
import pandas as pd

data = {}

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
    contact_nickname = input("Enter contact id: ").strip()
    name = input("Enter contact name: ").strip()
    while not name.isalpha():
        name = str(input('Please enter a valid name: '))
    surname = input("Enter contact surnamename: ").strip()
    while not surname.isalpha():
        surname = str(input('Please enter a valid surname: '))
    phone_number = input("Enter contact phone_number: ").strip()
    while not surname.isdigit():
        phone_number = str(input('Please enter a valid phone_number: '))
    age = input("Enter contact age: ").strip()
    while not age.isalpha():
        age = str(input('Please enter a valid age: '))

    data[contact_nickname] = {'name': name, 'surname': surname,
                                'phone_number': phone_number,
                                'age': age}
    print()

#Function to remove contact from the adress book
def remove_contact():
    print()
    contact_nickname = input("Enter contact_nickname to be deleted: ")
    del data[contact_nickname]
    print("contact removed.")
    print()

#Function to calculate number of contacts in the adress book
def calculate_number_of_contacts():
    print()
    print('Your number of contacts is {}'.format(len(data)))
    print()

#Function to search for the contact in the adress book
def search_contact():
    print()
    user_id = input("Please provide user_id : ")
    print()
    if user_id in data:
        print("user {} found in adress book: ".format(user_id))
        print("   %s." % data[user_id])
        print()
    else:
        print("User Not Found! Please provide a correct user_id")
        print()

#Function to list all contacts from the adress book
def list_all_contacts():
    print()
    print("Twoja lista kontaktow:")
    for k, v in data.items():
        print(k, v)
        print()

while True:
    start_menu()