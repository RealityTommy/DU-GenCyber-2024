'''
Password Manager
'''

# secret formula to encrypt password by moving one letter over in the alphabet
secretmap = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m", "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": "a"}

# dictionary of logins
logins = {}

'''
Functions
'''

# encrypt string
def encrypt(raw_password):
    encrypted_password = "" # empty string to hold encrypted password

    # loop through each letter in the raw password to encrypt
    for letter in raw_password:

        # find the key and add the value to the encryped password
        encrypted_password += secretmap[letter]

    # return encrypted password
    return encrypted_password

# decrypt string
def decrypt(encrypted_password):
    decrypted_password = ""  # empty string to hold decrypted password

    # loop through each letter in the encrypted password to decrypt
    for letter in encrypted_password:

        # loop through the secret map keys to find the ecrypted letter
        for key in secretmap.keys():

            # if the value matches the letter, add the key to the decrypted password
            if secretmap.get(key) == letter:
                decrypted_password += key

    # return the decrypted password
    return decrypted_password

# get all encrypted passwords
def get_encrypted_passwords():

    # check if there are any logins
    if logins.keys():

        # display login dictionary
        print(logins)

    else:
        print("No logins yet!") # inform user that there are no logins yet

# get list of all the logins
def get_usernames():

    # check if there are any logins
    if logins.keys():
    
        # loop through all the logins display usernames
        for login in logins.keys():
            print(login)
    
    else:
        print("No logins yet!") # inform user that there are no logins yet

# get unencrypted password from username
def get_password(username):

    # check if there's already a login for this username
    if logins.get(username):

        decrypted_password = decrypt(logins.get(username))  # decrypt password

        # provide user with decrypted password
        print("Password:", decrypted_password)
    
    else:
        # inform the user is there isn't a login
        print("There isn't a login for this username!")

# add a new login
def add_login(username, password):

    # check if there's already a login for this username
    if logins.get(username):

        # inform the user that the login already exists
        print("This login already exists.")
    
    else:
        encrypted_password = encrypt(password)  # encrypt password
        
        logins[username] = encrypted_password   # create new key value pair in logins dictionary

        print("Added new login for username:", username)    # inform user that login has been added

# remove a login
def remove_login(username):
    
    # check if there's already a login for this username
    if logins.get(username):

        logins.pop(username)    # remove key value pair from logins with username
        
        print("Removed login for username:", username)  # inform user that login has been removed
    
    else:
        print("There isn't a login for this username!") # inform the user is there isn't a login


'''
Interactable Program
'''

print("Welcome to Password Manager!")

print() # empty line for styling

while True:

    # let users know what options they have to interact with program
    print("Options:")
    print("1. See all encrypted passwords")
    print("2. See all usernames")
    print("3. Get password for a username")
    print("4. Add a login")
    print("5. Remove a login")
    print("6. Exit")

    print() # empty line for styling

    choice = input("Enter your choice (1-6): ") # get user option selection

    print() # empty line for styling

    # exit program
    if choice == "6":
        print("Exiting...")
        break

    elif choice == "1":

        # get all encrypted passwords
        get_encrypted_passwords()

        print() # empty line for styling

    # provide usernames
    elif choice == "2":
        print("Saved usernames:")
        get_usernames()

        print() # empty line for styling
    
    # get a password
    elif choice == "3":
        username = input("What's the username? ")   # get username from user

        password = get_password(username)

        print() # empty line for styling
    
    # add login
    elif choice == "4":
        username = input("What's the username? ")    # get username from user
        password = input("What's the password? ")    # get password from user

        add_login(username, password)   # add login

        print() # empty line for styling
    
    # remove login
    elif choice == "5":
        username = input("What's the username? ")    # get username from user

        remove_login(username)  # remove login

        print() # empty line for styling