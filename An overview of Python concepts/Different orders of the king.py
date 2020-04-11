i = input().split()
if i[0]=="food":
    if i[1]=="water":
        print("0.5")
    elif i[1]=="dinner":
        print("1.0")
elif i[0]=="promote":
    if i[1]=="judge":
        print("50.0")
    elif i[1]=="minister":
        print("80.0")
    elif i[1]=="governor":
        print("100.0")
elif i[0]=="travel":
    if i[1]=="ground":
        print("45.0")
    elif i[1]=="sea":
        print("58.0")
else:print("10.0")
