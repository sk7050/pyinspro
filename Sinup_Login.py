#small_Database
#Small_SinUp_Loging_system:

'''*****************SinUp & Login System****************'''

print("*********Wellcome to Sk Data System******")
get=int(input("What do you want!!? for SinUp Pess 1 or Login press 0:"))
database={}
c={}
def update_database():
   #Creat text File in_same_Directory as Name of data.txt
    with open("data.txt") as ref:
        for line in ref:
        	key,value=line.strip().split(",")
        	c[key]=int(value)
        	database.update(c)
        	
        	

    
    
def sinup(user_name,password,database):
    update_database()
    

    
    for i in database.keys():

        if(i==user_name):
            print(user_name,"not vaibable Please try with other User Name")
            sin_input()
            break
    else:
        newdata = open("data.txt", "a")
        newdata .write('%s,%d \n'%(user_name,password))
        print("sinup successfully ")
        newdata.close()
        update_database()
        log_input() 
        

def login(user_name,password,database):
    update_database()
    for i in database.keys():
                if(i==user_name):
                    if(password==database[i]):
                                    print("login Successfully") 
                                    break
                    else:
                        print("Possword is incorrect & Please try again")
                        log_input()
                        break
                        
                                    
    if(user_name in database.keys()):
        pass
    
    else:
        print("User Name is incorrect & Please try again")
        log_input()     
    
def sin_input():
    print("please input your Data for SinUP")
    user_name=input("Please input User Name:")
    password=int(input("Please input Password:"))
    sinup(user_name,password,database)
def log_input():
    print("please input your Data for Login")
    user_name=input("Please input User Name:")
    password=int(input("Please input Password:"))
    login(user_name,password,database)  

if (get==1):
    sin_input()

elif (get==0):
    log_input()
'''***********************************************'''
#
