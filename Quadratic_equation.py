


X=input("Please input Quadratic equation EX:--(x^2-2x+1)"+"\n"+":")

Op=[]


for m in X:
    if((m=="+") or (m=="-")):
        Op.append(m)
        continue
	
def plus_or_minus(X,Op):
    global a
    global b
    global c
    
    
    
    Y=X.split(Op[0])
    if(len(Y[0])==4):
                a=int((Y[0][0]))
    else:
    	a=1
    Z=Y[1].split(Op[1])
        
    if(len(Z[0])==2):
                b=int((Z[0][0]))
    else:
        b=1       
    
    c=int((Z[1]))
    if(Op[0]=="-"):
                b=-b
    if(Op[1]=="-"):
                c=-c
    

def minus_minus(X,Op):
    global a
    global b
    global c
        
        
    Y=X.split(Op[0])
      
    if(len(Y[0])==4):
            a=int((Y[0][0]))
            
    else:
        a=1
    
    
        
    if(len(Y[1])==2):
            b=int((Y[1][0]))
    else:
        b=1        
        
    c=int((Y[2]))
    if(Op[0]=="-"):
                b=-b
    if(Op[1]=="-"):
                c=-c
        
def All_plus_All_minus(X,Op):
    global a
    global b
    global c
    
    if(len(Op)==3):
            Y=X.split(Op[1])
            if(len(Y[1])==4):
                a=-int((Y[1][0]))
            else:
    	        a=-1
            if(len(Y[2])==2):
                b=int((Y[2][0]))
            else:
                b=1
            c=int((Y[3]))
            if(Op[1]=="-"):
                        b=-b
            if(Op[2]=="-"):
                c=-c 
    else:
            Y=X.split(Op[0])
            if(len(Y[0])==4):
                a=int((Y[0][0]))
            else:
    	        a=1
            if(len(Y[1])==2):
                b=int((Y[1][0]))
            else:
                b=1
            c=int((Y[2]))
            if(Op[0]=="-"):
                        b=-b
            if(Op[1]=="-"):
                        c=-c 
    


def mid_plus(X,Op):
    global a
    global b
    global c
        
        
    Y=X.split(Op[1])
        
    if(len(Y[0])==5):
                a=-int((Y[0][1]))
    else:
        a=-1
    Z=Y[1].split(Op[2])
        
    if(len(Z[0])==2):
                b=int((Z[0][0]))
    else:
        b=1        
        
    c=int((Z[1]))
    if(Op[1]=="-"):
                b=-b
    if(Op[2]=="-"):
                c=-c

def mid_plus_plus(X,Op):
    global a
    global b
    global c
        
        
    Y=X.split(Op[1])
       
    if(len(Y[0])==5):
            a=-int((Y[0][1]))
            print(a)
    else:
        a=-1
    
    
        
    if(len(Y[1])==2):
            b=int((Y[1][0]))
    else:
        b=1        
        
    c=int((Y[2]))
    if(Op[1]=="-"):
                b=-b
    if(Op[2]=="-"):
                c=-c
    
def mid_minus(X,Op):
    global a
    global b
    global c
        
        
    Y=X.split(Op[1])
        
    if(len(Y[1])==4):
            a=-int((Y[1][0]))
    else:
    	a=-1
    Z=Y[2].split(Op[2])
        
    if(len(Z[0])==2):
            b=int((Z[0][0]))
    else:
        b=1        
        
    c=int((Z[1]))
    if(Op[1]=="-"):
                b=-b
    if(Op[2]=="-"):
                c=-c
    

if(len(Op)==3):
    if(Op[0]!=Op[1] and Op[2]==Op[1]):
        mid_plus_plus(X,Op)

    elif(Op[0]==Op[1]==Op[2]=="-"):
        All_plus_All_minus(X,Op)
    elif(Op[1]=="+"):
        if((Op[2])=="-"):
            mid_plus(X,Op)
    
    elif(Op[1]=="-"):
        if((Op[2])=="+"):
            mid_minus(X,Op)
    
          
                    
            
else:
    if(Op[0]==Op[1]=="+"):
        All_plus_All_minus(X,Op)
    elif(Op[0]!=Op[1]):
        plus_or_minus(X,Op) 
    else:minus_minus(X,Op)    

               
               



def solv(a,b,c):

    A=((b**2)-(4*a*c))**(1/2)
    
    if(type(A)==complex):
                    print("The equation has no real roots"+"\n")
    elif(type(A)==int or type(A)==float):
        if(A>=0):
            x1=(-b+A)/2*a 
            x2=(-b-A)/2*a
            if(x1==x2):
                print("Solve of Quadratic equation"+" "+X+" "+"is")
                print("X="+str(x1)+"\n") 
            else:
                print("Solve of Quadratic equation"+" "+X+" "+"is")
                print("X="+str(x1)+" "+"AND"+" "+"X="+str(x2)+"\n")     
        
        else:
        
            print("The equation has no real roots"+"\n")

print("*****************************************************")
solv(a,b,c)
print("*****************************************************")