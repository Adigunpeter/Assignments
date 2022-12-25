class Add():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calc(self):
        print(self.x + self.y)

class sub():
   def __init__(self, x, y):
       self.x = x
       self.y = y  
   def calc(self):
       print(self.x - self.y)
        
   

class Mul():
   def __init__(self, x, y):
       self.x = x
       self.y = y  
   def calc(self):
       print(self.x * self.y)


class Div():
   def __init__(self, x, y):
       self.x = x
       self.y = y  
   def calc(self):
       print(self.x / self.y)

class ref:
      def __init__(self, x,):
        self.x = x

def calc(self): 
     if self.x ==1:
         return 1
     else:
         return(self.x * ref(self.x-1))

class perm():
       def __init__(self, x,  y):
        self.x = x
        self.y = y
       def calc(self):
        print(ref(self.x) / ref(self.y))

class comb():
       def __init__(self, x,  y):
        self.x = x
        self.y = y
       def calc(self):
        print(ref(self.x) / ref(self.y)*ref(self.x))
    

print("______welcome to Peter math function claculation _______")
print("1. ADDITION\n 2.SUB\n 3. Mul\n 4. Div\n 5. perm\n 6.comb")
ask = input("Enter any  alculation of your choice here>>")

if ask == "1":
        first = int(input("Enter your value here>"))
        second = int(input("Enter your value here>"))
        # add = Add(first, second)
        # add.calc()
        result = Add(first, second).calc()
        print(result)

elif ask == "2":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    result = sub(first, second).calc()
    print(result)


elif ask == "3":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    result = Mul(first, second).calc()
    print(result)

elif ask == "4":
    first = int(input("Enter your value here>"))
    second = int(input("Enter your value here>"))
    result = Div(first, second).calc()
    print(result)


elif ask == "5":    
    num=int(input("ENTER>> "))
    den=int(input("ENTER>> "))
    okay = perm(num,den).calc() #Permutation
    print(okay)

elif ask == "6":
    num=int(input("ENTER>> "))
    den=int(input("ENTER>> "))
    okay = comb(num,den).calc() #combination
    print(okay)

else:
    print("error")  
