#rolodexDict = {'phony' : {'name' : 'Phony Phony', 'phone' : 'PhonyNum', 'adress' : 'Pony adress'}}
rolodexDict = {'name' : 'nombre', 'phone' : 'numbero', 'adress' : 'direction'}
def addContact():
    global rolodexDict
    name = input('Fullname of the contact \n : ')
    adress = input('What is the Address of the contact? \n : ')
    phone = input('What is their phone number \n : ')
    rolodexDict.update( {'name' : name, 'phone' : phone, 'adress' : adress})
    print(name +' has been added to your Online Rolodex!!')
    main()
 
#def printRolo() :
    #global rolodexDict
    #for name,phone,adress in rolodexDict.items():
        #print ("\n---------------------------------------------------------")
        #print (str("Name: ") + str(name))
        #print (str("Number: ") + str(phone))
        #print (str("Address: ") + str(adress))
        #print ("---------------------------------------------------------\n")
    #print('\nName: %s\nPhone Number: %s\nAdress: %s\n' %(rolodexDict[i]['name'], rolodexDict[i]['phone'], rolodexDict[i]['adress']))
def searchContact():
    name = input('Type the person\'s name or nickname\n - ')
    for i in rolodexDict:
        if i.lower() == name.lower() or rolodexDict[i]['name'].lower() == name.lower():
            print('\nName: %s\nPhone Number: %s\nAdress: %s\n' %(rolodexDict[i]['name'], rolodexDict[i]['phone'], rolodexDict[i]['adress']))
        else:
            print('Name not found')
         

 
def main():
    print('Welcome to your online Rolodex !')
    print('** Choose from these options: **')
    print('*********1.Add Contact *********')
    #print('********2.Print Roledex ********')
    print('********3.Search Contact *******')
    #print('*******4.Remove Contact ********')
    print('********5.Exit Program *********')
    case = str(input('\n'))
    if case == '1':
        print('works')
        addContact()
    #elif case == '2':
        #print('works')
        #printRolo()
    elif case == '3':
        print('works')
        #addPerson()
    #elif case == '4':
        #print('works')
        
    elif case == '5':
        print('Thank you! Good Bye!!')
        quit()
    else:
        print('Invalid choice! Choice must be between 1-5: ')
        quit()
main()

