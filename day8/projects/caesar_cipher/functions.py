import alphabet
import os

def clear():
    os.system("clear")
        
def encrypt(text, shift):
    cipher = ""
    for char in text:
        if char.isalpha():
            position = alphabet.alphabet.index(char)
            new_pos = position + shift
            if new_pos > 25:
                new_pos -= 26
                cipher += alphabet.alphabet[new_pos]
            else:
                cipher += alphabet.alphabet[new_pos]
        else:
            cipher += char
    clear()
    print(cipher)


def decrypt(cipher, shift):
    text = ""
    for char in cipher:
        if char.isalpha():
            position = alphabet.alphabet.index(char)
            new_pos = position - shift
            if new_pos < 0:
                new_pos += 26
                text += alphabet.alphabet[new_pos]
            else:
                text += alphabet.alphabet[new_pos]
        else:
            text += char
    clear()
    print(text)

def caesar(text, shift, direction):
    text_new = ""
    for char in text:
        if char.isalpha():
            position = alphabet.alphabet.index(char)
            if direction == "encode":
                new_pos = position + shift
                if new_pos > 25:
                    new_pos -= 26
            elif direction == "decode":
                new_pos = position - shift
                if new_pos < 0:
                    new_pos += 26
            else:
                print("You need to choose encode/decode. Try again.")
            text_new += alphabet.alphabet[new_pos]
        else:
            text_new += char
    clear()
    print(f"{direction}d text is {text_new}")