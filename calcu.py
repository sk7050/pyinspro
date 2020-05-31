print("***Welcome to Calculating Program***")
print("###Please Do your calculating task###")
Data=[]
Output=0
Oparator=["+"]
Task=[input("You have to use Space bar to write Numbers or Operators"+"\n"+"Example(10 + 20 - 30)"+"\n"+":")]
temp=Task[0]
Separator=temp.split(" ")
for i in Separator:
    if ((i=="+") or (i=="-") or (i=="*") or (i=="/")):

        Oparator.append(i)
        continue
    Data.append(i)
    
for i in range(len(Data)):
   
    if (Oparator[i]=="+"):
       Output=Output+int(Data[i])
    elif (Oparator[i]=="-"):
        Output=Output-int(Data[i])
    elif (Oparator[i]=="*"):
        Output=Output*int(Data[i]) 
    elif (Oparator[i]=="/"):
        Output=Output/int(Data[i])   

print("************************"+"\n"+"OUTPUT"+"\n"+temp+" = "+str(Output))
