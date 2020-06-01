year = int(input("Enter a year: "))
if(year%4==0):
    if(year%400==0):
        if(year%100==0):
            print(year,"is leap Year")
          
        print(year,"is leap Year") 
    print(year,"is leap Year")     
else:
    print(year,"is comon year")
            