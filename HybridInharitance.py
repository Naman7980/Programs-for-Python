class base:
    def __init__(self,num1,num2):
        self.num1 = 1
        self.num2 = 2

class b1(base):
    def add(self):
        return self.num1 + self.num2
        

class b2(base):
    def subtract(self):
        return self.num1 - self.num2

class b3(b1,b2):
    def user(self):
        print(self.subtract())
        print(self.add())
    
a = b3(2,5)
a.user() 