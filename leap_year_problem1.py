year = int(input("Enter a year: "))
ref=[4,400,100]
for i in ref:
    if(year%i==0):
        print(year,"is leap Year")
        break
    else:
        print(year,"is comon Year")
        break