import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print("Original list:",chars)
print("Shuffled list:",key)

#encrypting....
while True:
    plain_text = input("Enter the text:")
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]    #exchanging the letters at same index
        
    print(f"Plain text :{plain_text}")
    print(f"Cipher text is :{cipher_text}")
        
#decryption.....
    cipher_text = input("Enter the text:")
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Cipher text :{cipher_text}")
    print(f"Plain text :{plain_text}")