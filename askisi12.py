"""
12. Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο
ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα του
στον “κατοπτρικό” του χαρακτήρα ASCII. Κατοπτρικοί χαρακτήρες
είναι αυτοί των οποίων το άθροισμα είναι 128.
Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.

"""


var_file="two_cities.txt"

M=""


f1=open(var_file,"r",encoding='utf-8')

flag=1
while flag:


    x=f1.readline()
##    print(x)
    if x=="":
        flag=0
    else:
        for c in x:
            ordc=ord(c)
            #print(ordc,end=',')
            ordc128=128-ord(c)
          
            
            if ordc128 >=0 and ordc128 <=128:
                newchar=chr(ordc128)
                M=newchar+M
                #print(newchar,end='')

##            if len(M) > 100 :
##                print(M)
##                M=""
    
    
f1.close()

print('len M:',len(M))

print(M)
