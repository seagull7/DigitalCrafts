book = {}

def one():
    who = raw_input("Type \'back\' to go back to the main menu. \nName: ")
    if who == "back":
        PhoneBook()
    elif book.get(who) != None:
        print ("\nFound entry for " + who + ": " + book.get(who))
        PhoneBook()
    else:
        print ("\nEntry not found, please try again: ")
        one()

        

def two():
    nName = raw_input("Name: ")
    nPhone = raw_input("Phone Number: ")
    book[nName] = nPhone
    print("Entry Stored for " + nName + "\n")
    PhoneBook()

def three():
    nName = raw_input("Type \'back\' to go back to the main menu. \nName: ")
    counter = 0
    if nName == "back":
        PhoneBook()
    elif nName in book:
        del book[nName]
        print ("Deleted entry for " + nName)
        print ("\n")
        PhoneBook()
    else:
        print ("Entry not found, please try again: ")
        three()

def four():
    if book == {}:
        print ("\nYour adress book is empty, try putting something in it first!")
        PhoneBook()
    for nName, nNumber in book.items():
        print ("\nFound entry for " + nName + ": " + nNumber + "\n")
    PhoneBook()

def five():
    print ("Bye.\n")


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
    else:
        print("Command not recognized:")
        PhoneBook()

PhoneBook()
