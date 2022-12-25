

# from fil1 import Father

# m = Father()





# print(f.name, f.age, f.car)

# print(paul(8))

# print(m.walk())





######simple


from fil1 import Mymath

m = Mymath()


print("____________welcome to paul calculator_________\n1. addit \n2. sub \n3. multi")

ask = int(input("Calculate>>"))

if ask == 1:
    """This function add two numbers toghter"""
    num = int(input("Enter any number here>>"))
    num2 = int(input("Enter any number here>>"))
    print(m.add(num, num2))

elif ask == 2:
    num = int(input("Enter any number here>>"))
    num2 = int(input("Enter any number here>>"))
    print(m.sub(num, num2))
elif ask == 3:
    num = int(input("Enter any number here>>"))
    num2 = int(input("Enter any number here>>"))
    print(m.mul(num, num2))
