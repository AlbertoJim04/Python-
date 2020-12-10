
#INF360 - Programming with Python
#Alberto Jimenez
#12/09/2020
#Final Project

'''
20 Points- Does the program execute with no errors.
20 Points- The program should contain: Good flow control, good use of functions,
        code should be as clean as possible (i.e. writing the smallest amount
        of code necessary to complete the function), and contain examples
        of lists or dictionaries.
20 Points- The project should be well documented. Make use of block and line
        comments to describe the program as a whole, individual functions,
        and major areas of the project.
20 Points- Use of the logging module. This should be used in place of where you
        might have had print statements (unless your project was intended to
        have console output. Refer to Chapter 10 – Debugging. You should
        import the module, setup the basic config, and then you must have a
        combination of logging.debug and logging.critical statements used
        appropriately. You can use any additional logging level you choose,
        possibly logging.warning
20 Points- Use of Object-Oriented Programming. This can be you creating your
        own classes and modules OR the use of third party modules. If using
        third party modules, be sure to put in the comments the
        packages that need to be installed (probably from pip).

'''
#import sys for the sys.exit()
import sys

#Import logging module for debugging
import logging
logging.basicConfig(filename='programlog.txt',level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')

#import functions.py page
try:
    import functions as fn
    logging.debug('functions.py file imported succefully')
except:
    logging.critical('Missing functions.py')
    logging.critical(' functions.py NOT Found, Please make sure file is in the same Directory ! program now closing')
    sys.exit()


logging.info('Displays the welcoming page as well as options to choose from')
def main():
    while True :
        print('Welcome to your online Rolodex !')
        print('** Choose from these options: **')
        print('*********1.Add Contact *********')
        print('********2.Print Roledex ********')
        print('********3.Search Contact *******')
        print('********4.Exit Program *********')
        case = str(input('\n'))
        if case == '1':
            fn.addContact()
        elif case == '2':
            fn.printRolo()
        elif case == '3':
            fn.searchList()
        elif case == '4':
            print('Thank you! Good Bye!!')
            sys.exit()
        else:
            logging.debug('User did not input correctly Choice must be between 1-4:')
            print('INVALID choice! Choice must be between 1-4: ')




main()
