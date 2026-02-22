import string 

def encrypt (message,list_alphabet,shift_number):
    encrypt_list=[]
    for char in message:
        if char == ' ':
            encrypt_list.append(char)
        elif char in list_alphabet:
            indice = list_alphabet.index(char)
            indice = (indice + shift_number) % len(list_alphabet)
            encrypt_list.append(list_alphabet[indice])
        else:
            encrypt_list.append(char)
    return ''.join(encrypt_list)
def decrypt (message,shift_number,list_alphabet):
    decrypt_list=[]
    for char in message:
        if char == ' ':
            decrypt_list.append(char)
        elif char in list_alphabet:
            indice = list_alphabet.index(char)
            indice-=shift_number
            decrypt_list.append(list_alphabet[indice])
        else:
            decrypt_list.append(char)
    return ''.join(decrypt_list)


alphabet_string = string.ascii_uppercase
alphabet_list = list((alphabet_string).lower())

action = False
while not action:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or Exit: \n").lower()
    if direction == "exit":
        break
    elif direction == "encode":
        text = input(("Type your message: \n")).lower()
        shift = int(input("Type the shift number : \n"))
        encrypt_word=encrypt(text,alphabet_list,shift)
        print(f"Encrypted message: {encrypt_word}")
    elif direction=="decode":
        text = input(("Type your message: \n")).lower()
        shift = int(input("Type the shift number : \n"))
        decrypt_word=decrypt(text,shift,alphabet_list)
        print(f"Unencrypted message: {decrypt_word}")
    else:
        print("Invalid Option. Try Again!!")