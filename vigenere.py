#!/usr/bin/python

def encrypt_string():
    word = input('Enter a word: ').strip()
    key = input('Enter a key: ').strip()
    cipher = cipher_word(word, key)
    print(cipher)
       
def cipher_word(word, key):
    key_length = len(key)
    cipher = ""
    for i, letter in enumerate(word):
        letter_code = ord(letter)
        key_code = ord(key[i % key_length]) 
        new_code = (letter_code + key_code ) % 26 + 65
        cipher += (chr(new_code))
    return cipher

def decipher_word(word_encrypted, key):
    original_word = ""

    
    

if __name__ == "__main__":
    encrypt_string()

