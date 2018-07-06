import string

def code_to_encrpyt():
    print "This program will encode your messages using a Caesar Cipher"
    print ""
    
    key = 3
    key = int(key)
    message = raw_input("Enter the message: ")
    
    for letter in message:
            print chr(ord(letter) + key)
    
code_to_encrpyt()

