from cryptography.fernet import Fernet
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)


#Run the below code first to create key.key file
#make the function load_key() and key and fer as comment before doing that and make this code comment again i.e write_key() and the calling

'''

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()

'''

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    '''
    file = open('passwords.txt", 'a)
    file.close()
    '''
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode()+ "\n") 



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password: ",fer.decrypt(passw.encode()).decode())



while True:
    mode = input("Would you like to add a new password or view existing ones(view, add)? or Q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
