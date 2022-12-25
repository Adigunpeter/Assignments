class Mymath():
    def __init__(self):
        self.pi = 3.1434455666
        # self.x = x
        # self.y = y


    def add(x,y):
        return x + y

    def sub( x, y):
        return x - y
       

    def mul( x, y):
        return x * y

    def div( x, y):
        return x / y

    def ref(x): 
     if x ==1:
         return 1
     else:
         return(x * Mymath.ref(x-1))

    def perm( x, y):
        return(Mymath.ref(x) / Mymath.ref(y))

    def comb( x, y):
         return(Mymath.ref(x) / Mymath.ref(y)) * (Mymath.ref(x))


    