from cryptography.fernet import Fernet

#admin password : abracadabra
x=input("enter password to login : ")

#commented because used to generate key only once
# def write_key():
#     key=Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()
def load_key():
    with open("key.key","rb") as f:
        key=f.read()
        return key







key=load_key()
fer=Fernet(key)


while x=="abracadabra":
    mode=input("do you want to add new password or view saved ones or quit (view/add/q) : ").lower()

    def add():
        user_name=input("enter user name : ")
        password=input("enter password : ")
        file_name="passwords.txt"
        with open(file_name,"a") as f:
            f.write(user_name+" | "+fer.encrypt(password.encode()).decode()+"\n")
    def view():
        file_name="passwords.txt"
        with open(file_name,"r") as f:
            lines=f.readlines()
            for line in lines:
                data=line.strip()

                user,passkey=data.split("|")
                print("user : ",user,"### password : ",fer.decrypt(passkey.encode()).decode())





    if mode=="add":
        add()
        continue
    elif mode=="view":
        view()
        continue
    elif mode=='q':
        quit()
    else:
        print("invalid mode")
        continue