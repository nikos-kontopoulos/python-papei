"""
13. Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου,
το χωρίζει σε λέξεις και εμφανίζει τα ζευγάρια λέξεων όπου το συνολικό τους μήκος
χαρακτήρων είναι ακριβώς 20. Κάθε ζευγάρι φεύγει από το σύνολο και το
πρόγραμμα τελειώνει όταν εξαντληθούν τα ζευγάρια.
Για το κείμενο "Tale of two cities" που υπάρχει στα έγγραφα,
δείγμα λέξεων που μένουν ανά μήκος: '12': [], '10': [], '15': [], '13': [],
'11': [], '14': [], '16': [], '18': [], '19': [],
'17': [], '20': ['carriagedoortenderly', 'thingnothingstartles']

"""




import os.path
import string
import random

#**************************
def clear_word(word):
    """
    καθαρίζει το 1ο ή το τελευταίο γράμμα κάθε λέξης
    αν δεν είναι γράμμα ή αριθμός
    """

    flag=1
    while flag:

        flag=0
        if  len(word) > 0 :
            if (word[0] not in string.ascii_letters and word[0] not in string.digits) :
                word = word[1:]
                flag=1
            
        if  len(word) > 0 :        
            if (word[-1] not in string.ascii_letters and word[-1] not in string.digits) :
                ln = len(word)
                word = word[0:ln-1]
                flag=1

    return word
#**************************

var_file="two_cities.txt"

if not os.path.isfile(var_file):
    print("Δε βρέθηκε το αρχείο")
else:

    M=[]
    N=[]
    for i in range(20):
        M.append([])

##    print(M)


    f1=open(var_file,"r",encoding='utf-8')

    flag=1
    while flag:


        x=f1.readline()
        
        if x=="":
            flag=0
        else:
            y=x.split()
            for item in y:
                if len(item) < 20:
                    item = clear_word(item)
                    if len(item) > 0:    
                        M[ len(item) ].append(item)
        
        
    f1.close()

##    print('len M:',len(M))

    for i in range(len(M)):
        random.shuffle( M[i] )
        N.append( len(M[i]) )

    for i in range(1,11):
        while len(M[i]) > 0 and len(M[20-i]) > 0 and len(M[10]) > 1:
            if i != 10:
                print( M[i][0] ," - ", M[20-i][0]," - ",i,20-i )
                M[i].pop(0)
                M[20-i].pop(0)
                
                
            elif i == 10 and len(M[i]) > 1:
                print( M[i][0] ," - ", M[i][1]," - ",i,20-i )
                M[i].pop(0)
                M[i].pop(0)
        print()

    print( '       Αρχικές  --  Τελικές' )
    print( '       λέξεις   --   λέξεις' )
    print( '------------------------------' )
    for i in range(len(M)):
        print( "{:0>2}".format( i )," - ", "{:>7,}".format( N[i] ), ' -- ', "{:>7,}".format( len(M[i]) ) )
            
