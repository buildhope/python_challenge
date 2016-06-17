#import string
import re

def find_char():
    content = open("regex_input.txt")
    contents = content.read()
    message = ''
    searchObj = re.findall(r'[^A-Z]([A-Z]{3})([a-z]{1})([A-Z]{3})[^A-Z]',contents,)
    if searchObj:
        for item in searchObj:
            if item[0] == item[2]:
                print item
        print searchObj
#        print "searchObj.group() : ", searchObj.group()
#        print "searchObj.group(1) : ", searchObj.group(1)
#        print "searchObj.group(2) : ", searchObj.group(2)
    else:
        print "Nothing found!!"
#    for i in contents:
#        if i in string.ascii_lowercase:
#            message = message + i
#    print message
    content.close()

find_char()

