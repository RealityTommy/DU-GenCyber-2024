# secret formula to encrypt password by moving one letter over in the alphabet
secretmap = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m", "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y", "y": "z", "z": "a"}

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

        # make a variable to track the letter to decrype
        previous_letter = letter

        # loop through the secret map keys to find the ecrypted letter
        for key in secretmap.keys():

            if key == letter:

                '''
                if the letter matches the key, we know the previous letter is the original,
                and add the value to the decrypted password
                '''
                decrypted_password += previous_letter
            
            else:
                # if the letter doesn't match the key, we replace the "previous letter" and move on
                previous_letter = key

    # return the decrypted password
    return decrypted_password
