import requests
import re
text = 'nothing'
# try http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=93781 if you dont want to run through all numbers
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
while 'nothing' in text or 'Divide' in text:
    r = requests.get(url)
    text = r.text
    if 'Divide by two' in text:
        print int(next_num[0])
        next_num[0] = int(next_num[0])/2
    else:
        next_num = re.findall(r'nothing.* (\d+)',r.text)
    
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(next_num[0])
    print next_num
    print 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(next_num[0])
