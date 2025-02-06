# Aim: Write a Program to define a function that accepts roll number and returns whether the
#student is present or absent.
# Branch: COMPS
# Year: 2nd
# Sem: 4
# Subject:Python lab
# Name: Pathan Mugaira Zakeer
# UIN:231P084
# Roll No.:25
print("***************************")
print("Pathan Mugaira")
print("***************************")

def check(roll, attendance_list):
    if roll in attendance_list:
        print(f"Roll number {roll} is present")
    else:
        print(f"Roll number {roll} is absent")

def presentees():
    p = []
    no_of_students = int(input("Enter number of students: "))
    for i in range(1, no_of_students + 1):
        roll_no = int(input("Enter roll no: "))
        p.append(roll_no)
    print("List of present students is:", p)
    return p  # Return the list of present students

attendance_list = presentees()  # Get the list of present students
roll = int(input("Enter roll no to check: "))
check(roll, attendance_list)  # Check if the given roll number is present
