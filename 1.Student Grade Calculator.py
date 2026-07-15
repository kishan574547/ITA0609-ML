mark1=int(input("enter first marks"))
mark2=int(input("enter first marks"))
mark3=int(input("enter first marks"))
total=mark1+mark2+mark3
avg=total/3
if avg>=90:
    grade='a'
elif avg >=75:
    grade='b'
elif avg>=50:
    grade='c'
else:
    grade='d'
    print("total marks=",total)
    print("average marks=",avg) 
    print("grade=",grade)   
