import string

def find_char():
    content = open("rare.txt")
    contents = content.read()
    message = ''
    for i in contents:
        if i in string.ascii_lowercase:
            message = message + i
    print message
    content.close()

find_char()
