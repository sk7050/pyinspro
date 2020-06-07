print("\n")
F=[[" "for i in range (6)] for j in range(6)]
A=[[" "for i in range (6)] for j in range(6)]
I=[[" "for i in range (6)] for j in range(6)]
S=[[" "for i in range (6)] for j in range(6)]

L=[[" "for i in range (6)] for j in range(6)]

for row in range(6):
    for col in range(6):
        if((row==0 or (row==2 and col<3))or (col==0 and row<6)):
            F[row][col]="*"
			
for row in range (6):
    for col in range(5):
        if((row==0 and 0<col<4) or row==2) or ((col==0 or col==4 )and 0<row<6):
            A[row][col]="*"	

for row in range(6):
    for col in range(6):
        if(col==0 and row<6):
            I[row][col]="*"

for row in range(6):
    for col in range(6):
        if(row==0 or row==3 or row==5) or(col==0 and (row<3)) or (col==5 and (row>2)):
            S[row][col]="*"



for row in range(6):
    for col in range(6):
        if(row==5 or col==0):
            L[row][col]="*"

for i in range (6):
    for j in range(6):
        print(F[i][j],end=" ")
    print(end=" ")    
    for j in range(6):
           print(A[i][j],end=" ")
    print(end=" ")    
    for j in range(6):
           print(I[i][j],end="")
    print(end=" ")
    for j in range(6):
           print(S[i][j],end=" ")
    print(end=" ") 
    for j in range(5):
           print(A[i][j],end=" ")
    print(end=" ") 
    for j in range(6):
           print(L[i][j],end="")
    print()


print("\n")             