#Password is valid
import re 
def password_is_valid(password):

    flag = 0
    while True: 
        if (len(password)<8): 
            raise Exception('password should be longer than than 8 characters')
            break
        elif not re.search("[a-z]", password): 
            raise Exception('password should have at least one lowercase letter')
            break
        elif not re.search("[A-Z]", password): 
            raise Exception('password should have at least one uppercase letter')
            break
        elif not re.search("[0-9]", password): 
            raise Exception('password should at least have one digit')
            break
        elif not re.search( "[%_!)*+,'&#(@$]", password): 
            raise Exception('password should have at least one special character')
            break
        elif re.search("\s", password): 
            flag = -6
            break
        else: 
            flag = 0
            print("password is valid")     
            break
            
            
password_is_valid('pasR3#sword')  




#========================================Password_is_okay==================================================#

def password_is_ok(password):
    while True:
        if (len(password)<9):
            return False
        if not re.search("[a-z]", password):
            return False 
        elif not re.search("[A-Z]", password):
            return False
            
        else:
            return True
                
            break
                

                
                
password_is_ok("rQ@DFGG1h")
            






