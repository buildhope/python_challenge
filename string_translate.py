import string

def decode(cipher_text):
    alphabet = string.ascii_lowercase
    message = ''
    for letter in cipher_text:
        if letter in alphabet:
            ind = alphabet.index(letter)
            if ind == 24:
                message = message + 'a'
            elif ind == 25:
                message = message + 'b'
            else:
                message = message + alphabet[ind+2]
        else:
            message = message + letter
    print message


in_strings = raw_input("enter string: ")
print in_strings
decode(in_strings)
