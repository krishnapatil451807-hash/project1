# check the number is odd
# a= int(input(""))
# print("number is odd:", a%2!=0)
# check the age in days
# age=21
# print(f"{age}years = {age*365} days")
# take minute min and coverts it into hour and min
# min = int(input("write a min "))
# print(f"{min} is {min//60} hours {min%60} min")
# write a program to extract the last digit of an number using modulus 
# a=str(input(" "))
# print(f"{a} : last digit is {a%10}")
# role=input("enter the role " )
# age=int(input(" enter the age "))
# print(f"eligible:",age < 21 and role =="student")
# crete the two variable swap it  without a third variable using arithematic operation 
# a = 10 
# b = 20
# a = a+b
# b= a-b
# a= a-b
# print(f"a = {a} and b = {b}",)
# is_rainnig=False
# if is_rainnig==True:
#    print("rainning ouside")
# else:
#    print("not rannig")
#condition statement
# age=int(input("enter your age"))
# if age<18:
#     print("you are not eligible to vote")
# else:
#     print("you are eligible to vote")
#elseif statement exaple 
# n=int(input(" enter your number "))
# if n==1:
#     print("monday")
# elif n==2:
#     print("tuesday")
# elif n==3:
#     print("wednsday")
# elif n==4:
#     print("thusday") 
# elif n==5:
#     print("friday") 
# elif n==6:
#     print("saturday")
# elif n==7:
#     print("sunday")  
# else:
#     print("enter valid number")    
# a = int(input(" enter your number "))
# if a/2==0:
#     print("even")
# else:
#     print("odd")
# age=int(input("enter your age "))
# price=int(input("enter the price "))
# if age<=12:
#     d=price*10/100
#     print(price-d)
# else:
#     print(price)
# on the base of the percentage mark and grade
# mark=int(input("enter your marks "))
# if 100>=mark>90:
#     print("o")
# elif 90>=mark>80:
#     print("a")
# elif 80>=mark>65:
#     print("35")
# elif 65>mark>=35:
#     print("c")
# elif 0<mark<35:
#     print("better luck next time")
# else:
#     print("enter valid marks "
#check the number is postive or negative 
# n= int(input("enter your number"))
# if n<0:
#     print("negative")
# elif n>0:
#     print("positive")
# else:
#     print("zero")
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# c=int(input("enter your number"))
# if a>b and a>c:
#    print(f"a isgreater{a} ")
# elif b>a and b>c:
#     print(f"b is greater {b}")
# elif c>a and c>a:
#     print(f"c is greater{c}")
# caluate leap year 
# 

# make a simply calculator using match case
a=int(input())
operat=(input())
b=int(input())
match operat:
   case'+':
    print(a+b)
   case '-':
    print(a-b)
   case'*':
    print(a*b)
   case'/':
    if b==0:
      print("enter valid number")
    else:
      print(a/b)
   case _:
    print("enter valid syntax")