# ascii_value = ord(v) # 118
# string_value = chr(ascii_value) # v




def encrypt():
    message = input("Enter the message you want to encrypt:")
    ascii_message = [ord(char)+3 for char in message]
    encrypt_message = [ chr(char) for char in ascii_message]
    print (''.join(encrypt_message))

def decrypt():
    message = input("Enter the message you want to decrypt:")
    ascii_message = [ord(char)-3 for char in message]
    decrypt_message = [ chr(char) for char in ascii_message]
    print (''.join(decrypt_message))


def again():
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice == 'e' or choice=='E':
        encrypt()
    elif choice == 'd'or choice=='D':
        decrypt()
again()
play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
if play_again == 'Y':
    i=1
    while i>0:
        again()
else:
    print("OK")
