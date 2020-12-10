#functions.py
'''Contains Object Contact custom class
   Contains list of all the objects added
   Contains all functions
'''


#initialized- contlist its a list of all the contacts in you Rolodex
contlist = []


#Searches and checks if the contact's first name exsits in your Rolodex
def searchList() :
    print("What is the First Name of the Contact youre looking for?: ")
    name = input()
    for i in contlist:
        if i.name == i.name:
            print("Your contact exists in your Rolodex ")
            break

    else :
        print("Sorry, Contact not Found")


#Prints out list of all objects. Contacts and numbers
def printRolo() :
     for i in range(len(contlist)):
        print("-----------------------------------")
        contlist[i].displayData()
        print("-----------------------------------")


#Adds contact information (name,number) to an Object list
def addContact() :

    class Contact(object):

        #'Contact Object initialized'
        def __init__ (self):
            print("Lets get started on your Rolodex.")


            self.Name = " "
            self.Number = " "
        #enterData function: Entering the Name and Number for the Object Contact
        def enterData(self):
            while True:
                print("Please enter the Contact name: ")
                name = input()
                #isalpha() Checks for onli a-z charachters allowed
                if name.isalpha() :
                    break
                else:
                    #logging.warning('Incorrect Format, You must type in the Contact Name')
                    print("Incorrect Format, You must type in the Contact Name")
            self.name = name

            while True:
                print("Please enter the Contact's Phone Number in 'xxxxxxxxxx' notation")
                number = input()
                #isdigit()Only allows \d for input
                if number.isdigit() :
                    break
                else:
                    #logging.warning("Incorrect Format,Please enter in valid format: 'xxxxxxxxx'.Only digits allowed. No white Spaces.")
                    print("Incorrect Format,Please enter in valid format: 'xxxxxxxxx'.Only digits allowed. No white Spaces. ")
            self.number = number

        #Function calls to print content in Object
        def displayData(self):
            print("Contact Name: ", self.name)
            print("Phone Number: ", self.number)



    #Loop that  appends New Object to List as well as saves and returns to main screen
    for i in range(1):
        a = Contact()
        a.enterData()
        contlist.append(a)
    #Prints out new contact
    for i in range(1):
        contlist[i].displayData()
        print("Was added to your Online Rolodex!!!")
        print("-----------------------------------")






#Ask Professor Zeller, Regex,Implementation recommendation
'''
def isPhoneNumber(number):
    while True :

        if len(number) != 12:
            return print('error code')
        for i in range(0, 3):
            if not text[i].isdecimal():
                return print('error code')
        if number[3] != '-':
            return print('error code')
        for i in range(4, 7):
            if not number[i].isdecimal():
                return print('error code')
        if number[7] != '-':
            return print('error code')
        for i in range(8, 12):
            if not text[i].isdecimal():
                return print('error code')
        return True
    return False
'''
