#Created by Manav Patni
#Program to find sum of n natural numbers

n = int(input("Enter any natural number here:- "))
num = n
sum = 0

if n <= 0: 
   print("Enter a whole positive number!") 
else: 
   while n > 0:
        sum = sum + n
        n = n - 1
    
print("Sum of first", num , "natural numbers is: ", sum)
