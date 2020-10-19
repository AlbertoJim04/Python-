#INF360 - Programming with Python
#Alberto Jimenez
#Midterm Project
'''
The purpose of this project is for the user to be able to Save 
Contact Information, Print contact list,for the FINAl version Id like to add 
Search or remove. 

Functionalities that are NOT quite there : 
As of now I am not able to add mpre than one contact in list/dictionary 
For the FINAl version, the project will be able to store multiple contacts as it should 

'''
import sys

#This is the contacts Dictionary
contacts = {'Name: ' : ' ', 'Phone #:' : ' ' }

#The add Contact function, that will later be able to add multiple contact 
def addContact():
    name = input('Full name of the contact \n : ')
    phone = input('What is their phone number \n : ')
    contacts.update({'Name: ' : name, 'Phone #:' : phone})
    print(name +' has been added to your Online Rolodex!!')

#Prints all contacts 
def printRolo() :
    print(contacts)
    

#Displays the welcoming page as well as options to choose from 
def main():
    while True :
        print('Welcome to your online Rolodex !')
        print('** Choose from these options: **')
        print('*********1.Add Contact *********')
        print('********2.Print Roledex ********')
        #print('********3.Search Contact *******')
        print('********4.Exit Program *********')
        case = str(input('\n'))
        if case == '1':
            addContact()
        elif case == '2':
            printRolo()
        #elif case == '3':
            #search()
        elif case == '4':
            print('Thank you! Good Bye!!')
            sys.exit(0)
        else:
            print('INVALID choice! Choice must be between 1,2 or 4: ')

main()
