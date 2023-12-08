import hashlib
import logging

logging.basicConfig(filename="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\myapp.log", encoding="UTF-8", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def register_user(username, password):
    try:
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        with open("users.txt","a") as users_file:
            users_file.write(f"{username}:{hashed_password}\n")
        print("user registered")
    except Exception as e:
        logging.error("error while registering: %s",e)
        print("error while regsitering ",e)

def authenticate_user(username, password):
    try:
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        with open("users.txt","r") as users_file:
            for line in users_file:
                stored_username, stored_password=line.strip().split(":")
                if username==stored_username and hashed_password==stored_password:
                    return True
        return False
    except Exception as e:
        logging.error("error occurred while logging: %s",e)
        print("error occurred while logging: ",e)
        return False

if __name__=="__main__":
    try:
        while True:
            print("1.Register\n2.Login\n3.Quit")
            choice=input("Enter choice: ")

            if choice=='1':
                username=input("Enter username: ")
                password=input("Enter password: ")
                register_user(username,password)
                print("User registered")

            elif choice=='2':
                username=input("Enter username: ")
                password=input("Enter password: ")
                if authenticate_user(username, password):
                    print("Login successfully")
                else:
                    print("Invalid credentials entered. login failed")

            elif choice=='3':
                print("thankyou")
                break

            else:
                print("Invalid choice. try again")

    except Exception as e:
        logging.error("Unhandled error: %s",e)


