# INF 360
#Alberto Jimenez
#Assignment 4
#Mad libs practice project


import re

#Create text file
madlib = open('madLib.txt', 'w')
#Create madlib sentece in text file
sentence = 'I saw a ADJECTIVE NOUN that ADVERB VERB a ADVERB NOUN the other day! Then a NOUN almost VERB me, becasue that NOUN ADVERB VERB! '
#Use .write to write in madLib.txt file
madlib.write(sentence)
# close txt file
madlib.close()


speech = re.split('(\W+)', sentence)
#Loops sentecne and scans for NOUN,Adverb,etc, and if so promts user input
for x in speech:
    if x == 'NOUN':
        speech.insert(speech.index('NOUN'), input('Replace ' + x + ': '))
        speech.remove('NOUN')
        #print(NOUN)
    elif x == 'ADJECTIVE':
        speech.insert(speech.index('ADJECTIVE'), input('Replace ' + x + ': '))
        speech.remove('ADJECTIVE')
    elif x == 'ADVERB':
        speech.insert(speech.index('ADVERB'), input('Replace ' + x + ': '))
        speech.remove('ADVERB')
    elif x == 'VERB':
        speech.insert(speech.index('VERB'), input('Replace ' + x + ': '))
        speech.remove('VERB')
speech = ''.join(speech)

#Print Madlib
print(speech)

