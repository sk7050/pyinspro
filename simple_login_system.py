user_name=input("Please input User Name:")
password=int(input("Please input Password:"))
youser={'faisal':123456,'Partha Sharothi':23457}

for i in youser.keys():
    if(i==user_name):
        for j in youser.values():
            if(password==youser[i]):
                    print("login Successfully") 
                    break
            else:
                print("Possword is incorrect & Please try again")
                break
if(user_name in youser.keys()):
    pass
else:
    print("User Name is incorrect & Please try again")
        
           