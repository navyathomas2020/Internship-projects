students=[]
n=int(input("Enter no.of students"))
for i in range(n):
    print("\ndetails of student",i+1)
    name=input("enter name")
    m1=int(input("enter marks of maths"))
    m2=int(input("enter marks of english"))
    m3=int(input("enter marks of science"))
    total=m1+m2+m3
    avg=total/3
    if avg>90:
        grade="A"
    elif (avg>80 and avg<90):
        grade="B"
    elif(avg>70 and avg<80):
        grade="C"
    else:
        grade="D"
    student={"Name":name,
         "marks":[m1,m2,m3],
         "sum":total,
         "average":avg,
         "grade":grade}
    students.append(student)
print("\n result of all students")
for s in students:
    print("\nname of student:",s["Name"])
    print("marks:",s["marks"])
    print("sum of marks:",s["sum"])
    print("average:",s["average"])
    print("grade",s["grade"])

search_element = input("Enter the name to be searched")
flag=0
for s in students:

    if s["Name"].lower()==search_element.lower():
        print("\nname of student:",s["Name"])
        print("marks:",s["marks"])
        print("sum of marks:",s["sum"])
        print("average:",s["average"])
        print("grade",s["grade"])
        flag=1
        break
    else:
        print("not found")
    