# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)   #type caste to a list
# key = chars.copy()    #copying the chars
# random.shuffle(key)   #shuffling chars

# print(f"chars : {chars}")
# print(f"key : {key}")


# #Encrypt
# plain_text = input("Enter a message to encrypt: ")
# cipher_text =  " "

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message: {plain_text}")
# print(f"encrypted message: {cipher_text}")

# cipher_text = input("Enter a message to decrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index=key.index(letter)
#     plain_text += chars[index]

# print(f"original message: {cipher_text}")
# print(f"encrypted message: {plain_text}")







# import random
# import string

# chars = " " + string.ascii_letters + string.digits + string.punctuation
# chars = list(chars)
# key = chars.copy()
# random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")


# while True:
# #Encrypt
#     plain_text =input("Enter a text to encrypt: ")
#     cipher_text = ""

#     for letter in plain_text:
#         index = chars.index(letter)
#         cipher_text += key[index]

#     print(f"plain_text: {plain_text}")
#     print(f"cipher_text: {cipher_text}")

#     #Decrypt
#     cipher_text = input("Enter a text to decrypt: ")
#     plain_text = ""

#     for letter in cipher_text:
#         index = key.index(letter)
#         plain_text += chars[index]

#     print(f"plain_text: {cipher_text}")
#     print(f"cipher_text: {plain_text}")









import random
import string

char = string.ascii_letters + string.digits
#type caste 
char = list(char)
#shuffle the characters
key = char.copy()
random.shuffle(key)


plain_text = input("Enter the text to decode:")
cipher_text =""
for letter in plain_text:

    index = char.index(letter)
    cipher_text += key[index]
print(f"The encrypted code is : {cipher_text}")

