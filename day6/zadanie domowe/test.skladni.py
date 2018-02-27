data = {'Murlock': {'name': 'Lukasz', 'surname': 'Malinowski', 'phone_number': '123456789', 'age': '33'},
        'Chittat': {'name': 'Stefan', 'surname': 'Jakotako', 'phone_number': '987654321', 'age': '31'},
        'Kanott': {'name': 'Grazyna', 'surname': 'Sprezyna', 'phone_number': '123987654', 'age': '22'}}

user_id = input("Please provide user_id : ").strip()
if user_id in data:
    print("user {} found in adress book".format(user_id))
    print("   %s." % data[user_id])
else:
    print("User Not Found! Please provide a correct user_id")


