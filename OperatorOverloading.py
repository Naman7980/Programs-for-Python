class Vector:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return f"{self.a}a + {self.b}b + {self.c}c"
    
    def __add__(self, x):
        return Vector(self.a + x.a, self.b + x.b, self.c + x.c)
    
v1 = Vector(2,5,7)
print(v1)     
v2 = Vector(1,4,5)
print(v2)
print(v1 + v2)
print(type(v1 + v2)) 
 


                      
                               
                               