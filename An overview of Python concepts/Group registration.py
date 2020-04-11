users = [
    ["email", "2A-^N#Hc"],
    ["mohamadreza33@gmailcom", "tQ$jk2?v"],
    ["alish007@gmail.com", "BBWyV#bh"],
    ["poooyan12/5@gmail.com","lWuw??xB"]
    ]
import hashlib
import re
def is_email_valid(email):
    if re.match(r"^([-\w]+)+@[A-Z*a-z\d]+(\.{1,1}\w{1,3})$", email):return True
    else:return False 

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def process_data(data):
    data = filter(lambda pair: is_email_valid(pair[0]), data)
    data = list(map(lambda t: (t[0], hash_password(t[1])), data))
    return data
print(process_data(users))