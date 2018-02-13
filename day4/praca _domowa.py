known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
hello = "Hi {}, have a nice day"

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").capitalize().strip()

    if name in known_users:
        print(hello.format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        else:
            print("not a problem. Fuck Off!")
    else:
        print(("I havent met you yet {}").format(name))
        add_me=input("would you like to be added to the system?: (y/n)").lower()
        if add_me =="y":
            known_users.append(name)
        else:
            print("kiwikiwikiwi")
