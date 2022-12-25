#name = ("pmath")
#def factorial(n):
#    if n == 0:
#         return 1
#     else:
#        return n * factorial(n-1)

def ref(x): 
     if x ==1:
         return 1
     else:
         return(x * ref(x-1))


print("______welcome to Peter math function claculation _______")
print("1. ADDITION\n 2.SUB\n 3. Mul\n 4. Div\n 5. perm\n 6.comb")
ask = input("Enter any  alculation of your choice here>>")

if ask == "1":
        first = int(input("Enter your value here>"))
        second = int(input("Enter your value here>"))
        print(first + second)

elif ask == "2":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    print(first - second)

elif ask == "3":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    print(first * second)

elif ask == "4":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    print(first / second)

#   elif ask == "5":
#   input = int(input("Enter your value here>"))
#   print(factorial(input))

elif ask == "5":    
    num=int(input("ENTER>> "))
    den=int(input("ENTER>> "))
    okay = ref(num)/ref(num-den) #combination
    print(okay)

elif ask == "6":
    num=int(input("ENTER>> "))
    den=int(input("ENTER>> "))
    okay = ref(num)/(ref(num-den) * ref(den)) #combination
    print(okay)

else:
    print("error")