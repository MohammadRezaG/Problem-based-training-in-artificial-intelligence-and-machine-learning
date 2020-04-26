import re
import math
var={}
class math2 (object):
    def add( a , b):
        a=float(a)
        b=float(b)
        return float(a+b)
    def sub( a , b):
        a=float(a)
        b=float(b)
        return float(a-b)
    def mul( a , b):
        a=float(a)
        b=float(b)
        return float(a*b)
    def div( a , b):
        a=float(a)
        b=float(b)
        return float(a/b)
    def pow( a , b):
        a=float(a)
        b=float(b)
        return math.pow(a,b)
    def gcd( a , b):
        a=int(a)
        b=int(b)
        return float(math.gcd(a,b))
    def log( a , b):
        a=float(a)
        b=float(b)
        return math.log(a,b)
while True:
    i=input()
    if ":="in i:
        i=i.replace(' ', '').split(":=")
        if re.fullmatch(r"[A-Z+a-z+\_]+",i[0]):
            if re.fullmatch(r"[\d+\.]+",i[1]):
                var[i[0]]=i[1]
            elif re.fullmatch(r"[A-Z+a-z+\_]+",i[1]):
                if i[1]in var:
                    var[i[0]]=var[i[1]]
                else:print('variable error')
            elif '(' in i[1] and ')' in i[1]:
                i[1]=i[1].replace('(',' ').replace(')','').split(' ')
                i[1][1]=i[1][1].split(',')
                if not(re.fullmatch(r"[A-Z+a-z+\_]+",i[1][1][0]) or re.fullmatch(r"[\d+\.]+",i[1][1][0])) or not(re.fullmatch(r"[A-Z+a-z+\_]+",i[1][1][1]) or re.fullmatch(r"[\d+\.]+",i[1][1][1])):
                    print('val is not a number')
                elif i[1][0]=='add' or i[1][0]=='sub' or i[1][0]=='mul' or i[1][0]=='div' or i[1][0]=='pow' or i[1][0]=='gcd' or i[1][0]=='log':
                    if (i[1][1][0]in var or re.fullmatch(r"[\d+\.]+",i[1][1][0])) and (i[1][1][1]in var or re.fullmatch(r"[\d+\.]+",i[1][1][1])):
                        if not re.fullmatch(r"[\d+\.]+",i[1][1][0]):
                            i[1][1][0]=var[i[1][1][0]]
                        if not re.fullmatch(r"[\d+\.]+",i[1][1][1]):
                            i[1][1][1]=var[i[1][1][1]]
                        var[i[0]]=getattr(math2,i[1][0])(float(i[1][1][0]), float(i[1][1][1]))
                    else:print('variable not found')
                    
                else:print("function not found")
            else:print('val is not a number')
        else:print('variable error')
    elif i == 'end':break
    else:
        if i in var:print("%.3f"%(float(var[i])))
        else:print("variable not found")