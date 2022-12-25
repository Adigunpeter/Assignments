def ref(x): 
     if x ==1:
         return 1
     else:
         return(x * ref(x-1))


def add(x,y):
    return x+y

def sub(x,y):
        return x-y   

def Mul(x,y):
        return x*y   

def Div(x,y):
        return x/y 



print("______welcome to Peter math function claculation _______")
print("1. ADDITION\n 2.SUB\n 3. Mul\n 4. Div\n 5. perm\n 6.comb")
ask = input("Enter any  alculation of your choice here>>")

if ask == "1":
        first = int(input("Enter your value here>"))
        second = int(input("Enter your value here>"))
        result = add(first,second)
        print(result)

elif ask == "2":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    result = sub(first,second)
    print(result)

elif ask == "3":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    result = Mul(first,second)
    print(result)

elif ask == "4":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    result = Div(first,second)
    print(result)


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