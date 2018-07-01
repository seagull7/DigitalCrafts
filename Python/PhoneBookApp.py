book = {}

def one():
    who = raw_input("Name: ")
    if book.get(who) != "None":
        print ("Found entry for " + who + ":" + book.get(who))
        PhoneBook()
    else:
        print ("Entry not found, please try again: \n")
        one()

def two():
    nName = raw_input("Name: ")
    nPhone = raw_input("Phone Number: ")
    book[nName] = nPhone
    print("Entry Stored for " + nName "\n")
    PhoneBook()

def three():
    nName = raw_input("Name: ")
    counter = 0
    if nName in book:
        del book[nName]
        Print ("Deleted entry for " + nName)
        print ("\n")
        PhoneBook()
    elif counter < 3:
        print ("Entry not found, please try again: ")
        three()
        counter +=1
    else:
        PhoneBook()

def four():
    for nName, nNumber in book.items():
        print ("Found enbtry for " + nName + ":" + nNuumber)
        print ("\n")
        PhoneBook()

def five():
    print ("Bye.")


def PhoneBook():    
    print("\nElectronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit ")
    menu = int(input("\nWhat do you want to do? (1-5) "))
    if menu == 1:
        one()
    elif menu == 2:
        two()
    elif menu == 3:
        three()
    elif menu == 4:
        four()
    elif menu == 5:
        five()

PhoneBook()
