from file3 import Mymath
m = Mymath

ask = input("ask>>")
num1 = int(input("Enter your first number here>>"))
num2 = int(input("Enter your second number here>>"))
if ask == "1":
    print(m.add(num1,num2))
elif ask =="2":
    print(m.sub(num1,num2))
elif ask =="3":
    print(m.mul(num1,num2))
elif ask =="4":
    print(m.div(num1,num2))
elif ask == "5":
    print(m.perm(num1,num2))
elif ask =="6":
    print(m.comb(num1,num2))
else: 
    print("error")