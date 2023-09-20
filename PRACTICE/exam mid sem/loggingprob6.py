import hashlib
import logging

logging.basicConfig(filename="myapp.log",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def register_user(username,password):
    try:
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        with open('users.txt','a') as users_file:
            users_file.write("User registered: %s\n", username)
    except Exception as e:
        logging.ERROR("error while registering user: %s",e)

def authenticate_user(username, password):
    try:
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        with open('users.text','r') as users_file:
            for line in users_file:
                stored_username, stored_password=line.strip().split(":")
                if username==stored_username and password==stored_password:
                    return True
        return False
    except Exception as e:
        logging.ERROR("Error while authenticating user: &s",e)
        return False
    
if __name__=="__main__":
    try:
        while True:
            print("1. Register\n2. Login\n3. Quit")
            choice=input("Enter your choice: ")

            if choice=="1":
                username=input("Enter username: ")
                password=input("Enter password: ")
                register_user(username,password)
                print("User registered successfully")

            elif choice==2:
                username=input("Enter username: ")
                password=input("Enter password: ")
                if authenticate_user(username, password):
                    print("Login Successful")

                else:
                    print("login failed. invalid credentials")

            elif choice =='3':
                print("Existing")
                break

            else:
                print("Invalid choice please choose again")
    except Exception as e:
        logging.ERROR("Unhandled error: %s",e)

