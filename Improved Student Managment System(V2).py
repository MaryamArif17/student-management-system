students = []

def add_student(name,marks):
    student = {"name": name, "marks":marks}
    students.append(student)
   

def display_student():
    for student in students:
        print(student["name"],student["marks"])

def passed_student():
    for student in students:
        if student["marks"]>=50:
            print(student["name"],"Pass")
        else:
            print(student["name"],"Fail")
          

def total_student():
    count = 0
    for student in students:
        count=count+1
    print("Total Students are: ",count)


def avg_marks():
    total = 0
    for student in students:
        total = total+student["marks"]
    avg = total/len(students)
    print("The average marks are:" , avg)


def highest_marks():
    x =students[0]["marks"]
    for student in students:
        if student["marks"]>x:
            x=student["marks"]
    print("The highest marks are:", x)



add_student("Hira", 89)
add_student("Kura", 98)
add_student("Bisma", 45)
add_student("Rida", 50)
display_student()
passed_student()
total_student()
avg_marks()
highest_marks()