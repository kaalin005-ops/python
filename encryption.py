import random
import string

chars=" " + string.punctuation + string.digits +string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)

print(f"chars :{chars}")
print(f"keys  :{key}")

#ENCRYPT
plain_text=input("Enter a message to encrypt:")
cipher_text=" "
for letter in plain_text:
    index=chars.index(letter)
    cipher_text += key[index]
print(f"encrypted message:{cipher_text}")

#decrypt
def main(chars,key):
    decrypt=input("Enter the message to decrypt:")
    decrypt_text= ""
    for letter in decrypt:
        index=key.index(letter)
        decrypt_text+=chars[index]
        print(f"decrypted message:{decrypt_text}")
    return 0


if __name__=='__main__':
    main(chars,key)
