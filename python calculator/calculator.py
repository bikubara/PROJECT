#project: simple 2 digit calculator
#author: biku bara

def add(x,y):
 return x+y

def subtract(x,y):
 return x-y

def multiply(x,y):
 return x*y

def divide(x,y):
 return x/y

print("\n")
print("------------------------------------------------------------------------------------------")
print("SIMPLE CALCULATOR (two numbers)");
print("------------------------------------------------------------------------------------------")

choice=input("ENTER CHOICE( |1=add | 2=subtract | 3=multiply | 4=divide | ):")

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if choice=="1" :
    print(num1 ,' + ', num2, ' = ' , add(num1,num2))
    
elif choice=="2":
     print(num1 ,' - ', num2, ' = ' , subtract(num1,num2))
    
elif choice=="3":
     print(num1 ,' * ', num2, ' = ' , multiply(num1,num2))
     
elif choice=="4":
     print(num1 ,' / ', num2, ' = ' , divide(num1,num2))

else:
    print("you entered the incorrect argument")

