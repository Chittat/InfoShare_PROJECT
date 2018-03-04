films = {
    "Kubus Puchatke":[3,5],
    "KiwiKiwiKiwi":[18,5],
    "Janusze Biznesu":[15,5],
    "Cos":[12,5]}

while True:

    choice=input("What movie would you like to watch?: ").strip().title()

    if choice in films:
        age=int(input("how old are you?: ").strip())

        if age >= films[choice][0]:

            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("not enough of tickets")
        else:
            print("You are to young, BYE!")
    else:
        print("we dont have that film")