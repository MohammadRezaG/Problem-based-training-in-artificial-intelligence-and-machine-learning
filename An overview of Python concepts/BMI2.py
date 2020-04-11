def BMI(weight,height):
    #weight=float(weight)
    #height=float(height)
    height=float(height)/100
    return float((float(weight)/(height**2)))


def process(path):
    athletes,normal_people,a,n=[],[],[],[]
    with open(path, 'r+') as file: 
        for line in file:
            l=line.split()
            BMIt=BMI(l[1],l[0])
            if l[2]=="ATHLETE":
                athletes.append((l[0],l[1],BMIt))
                a.append(BMIt)
            else:
                normal_people.append((l[0],l[1],BMIt))
                n.append(BMIt)
    athletes_average_bmi= sum(a) / len(a)
    normal_average_bmi= sum(n) / len(n)
    return athletes , athletes_average_bmi , normal_people, normal_average_bmi
print(process(r"myfile.txt"))