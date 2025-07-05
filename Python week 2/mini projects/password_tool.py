import random
import string
import base64

# step 1 : password gen 
length = int(input("Enter the length of the password: "))

def genrate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    # print("Generated Password:", password)
    return password

# step 2 : encrpyt using base 64 (like 64 bit style string)
password = genrate_password(length)
def encrypt_password(password):
    encoded = base64.b64encode(password.encode('utf-8'))
    # print("Encrypted Password:", encoded.decode('utf-8'))
    return encoded.decode('utf-8')

# step 3 : decrypt
def decrypt_password(encoded_password):
    decoded = base64.b64decode(encoded_password.encode('utf-8'))
    # print("Decrypted Password:", decoded)
    return decoded.decode('utf-8')

# main program
def main():
    print ("welcome to password tool")
    password = genrate_password(length)
    print ("Generated Password:", password)
    encrypted = encrypt_password(password)
    print ("Encrypted Password:", encrypted)
    decrypted = decrypt_password(encrypted)
    print ("Decrypted Password:", decrypted)

    #verify
    if decrypted == password:
        print ("Password verified")
    else:
        print ("Password not verified")

# run the program

if __name__ == "__main__":
   main()

# encrypt_password(password)