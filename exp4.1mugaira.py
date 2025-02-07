# Aim: Write a Program to print no of lines in a file.
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
f_name=input("Enter file name:-  ")
num_line=0
with open(f_name,'r')as f:
    for line in f:
        num_line+=1
print("Number of lines:-")
print(num_line)
