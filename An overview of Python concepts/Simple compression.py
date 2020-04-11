F=open(r"myfile.txt", 'r+')
i=F.read()
c=0
d={}
c2=0
for x in i:
    c2+=1
    if c2/len(i)*100%5==0:
        print("%.0f"%(c2/len(i)*100))
    if len(d)==c:
        d[c]="{}1".format(x)
    elif not list(d[c])[0]==x:
        c+=1
        d[c]="{}1".format(x)
    elif c in d:
        d[c]="{}{}".format(d[c][0],int(d[c][1:])+1)
F.close()
F=open(r"myfile_compression.txt","w")
for x in d.values():
    F.write(x)
F.close()
print ("sucsess")
