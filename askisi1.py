import random

#******************************
def make_tetrades(lista):

    for i in range(0,len(lista)-3):
        m=[]
        for j in range(i,i+4):
            m.append(lista[j])
        M.append(m)

    return
#*******************************

#******************************
def count_tetrades():
    x=0
    for i in range(len(M)):
        y=sum(M[i])
        if y==4:
            x+=1
    print(times,x)
    return x
#******************************

tot_tetrades=0 

stiles = int(input("δώσε πλάτος τετραγώνου (>=4) : "))
grames = int(input("δώσε ύψος τετραγώνου   (>=4) : "))

for times in range(100):

    M = [] # Master table
    L = [] # τετράγωνο
    
    for i in range(grames):
        L1 = []
        for j in range(stiles):
            L1.append(0)
        L.append(L1)

    theseis = (grames * stiles)


    i=0
    while i <  theseis//2:
        x = random.randint(0,theseis-1)
        row = x // stiles
        col = x % stiles
        if L[row][col] == 0:
            L[row][col] = 1
            i+=1
        
    """
        for row in range(grames):
            print(L[row])
        print()
    """


    #***** Horizontal *****
    
    for row in range(0,grames):
        L1 = []
        for col in range(0,stiles):
            L1.append( L[row][col] )
        if len(L1) > 4:
            make_tetrades(L1)
        else:
            M.append( L1 )

    """
    print("horizontal")
    hor=len(M)
    for i in range(0,hor):
        print(M[i])
    """


    #***** Verical *****

    for col in range(0,stiles):
        L1 = []
        for row in range(0,grames):
            L1.append(L[row][col])
        if len(L1) > 4:
            make_tetrades(L1)
        else:
            M.append( L1 )

        

    """
    
    print("diagonia 1")

  
    L1=[]
    for row in range(0,diastash):
        L1.append(L[row][row])
    if len(L1) > 4:
        make_tetrades(L1)
    else:
        M.append(L1)
    """

    #***** 1η διαγώνιος *****
    
    row_var = 0
    col_var = 0
    fl = 0
    row = row_var

    for i in range(0,stiles):    

        L1  = []
        fl  = 0
        col = col_var
        while fl == 0:
            L1.append(L[row][col])
            
            row += 1
            col -= 1
            if row >= grames or col < 0 :
                fl=1
                
##        print(L1)
        if len(L1) > 4:
            make_tetrades(L1)
        elif len(L1) == 4:
            M.append( L1 )
        
        row=0
        col_var += 1

    row_var = 1
    col_var = stiles-1
    fl = 0
    for i in range(row_var,grames):

        L1 = []
        fl = 0

        row = row_var
        col = col_var
        while fl == 0:
            L1.append(L[row][col])
            
            row += 1
            col -= 1
            if row >= grames or col < 0 :
                fl=1
                
##        print(L1)
        if len(L1) > 4:
            make_tetrades(L1)
        elif len(L1) == 4:
            M.append( L1 )

        row_var += 1
        col_var = stiles-1    

            
    #***** 2η διαγώνιος *****

    row_var = grames-1
    col_var = 0
    fl = 0

    for i in range(0,grames):    

        L1  = []
        fl  = 0
        row = row_var
        col = col_var
        
        while fl == 0:
            L1.append(L[row][col])
            
            row += 1
            col += 1
            if row >= grames or col >= stiles :
                fl=1
                
##        print(L1)
        if len(L1) > 4:
            make_tetrades(L1)
        elif len(L1) == 4:
            M.append( L1 )

        row_var -= 1
        col_var  = 0

    row_var = 0
    col_var = 1
    fl = 0
    for i in range(1,stiles):

        L1 = []
        fl = 0

        row = row_var
        col = col_var
        
        while fl == 0:
            L1.append(L[row][col])
            
            row += 1
            col += 1
            if row >= grames or col >= stiles :
                fl=1
                
##        print(L1)
        if len(L1) > 4:
            make_tetrades(L1)
        elif len(L1) == 4:
            M.append( L1 )
        
        row_var = 0
        col_var += 1    

    tot_tetrades += count_tetrades()

print( tot_tetrades )   
print( round(tot_tetrades/100,2) )   
