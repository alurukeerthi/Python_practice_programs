t=int(input("Marks in Telugu: "))
e=int(input("Marks in English:"))
h=int(input("Marks in Hindi: "))
total=t+e+h
average=total/3
percentage=(total/300)*100

grade=" "
if percentage>=90:
    grade="A"
elif percentage>=80:
    grade="B"
elif percentage>=70:
    grade="C"
elif percentage>=60:
    grade="D"
else:
    grade="P"
    
print(f"Total marks:{total}\nAverage marks:{average}\nGrade:{grade}")
