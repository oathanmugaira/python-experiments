# Aim: Write a Program to Recursive function to calculate sum of a number from 0 to n.
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
def sum_recur(n):
    if n==1:
     return 1
    else:   
     return n+sum_recur(n-1)

n= int(input("Enter number:- "))
if n<=0:
 print("Enter positive number ")
else:
 print(" Sum is:- ", sum_recur(n))
 
