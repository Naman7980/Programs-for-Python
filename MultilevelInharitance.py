class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def showdetails(self):
        print(f"Name = {self.name}")
        print("Species = {self.species}")
        
class dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "dog")
        self.breed = breed
        
    def showdetails(self):

        Animal.showdetails(self)
        print(f"Breed: {self.breed}")                
            
class golden_retriever(dog):
    def __init__(self, name, color):
        dog.__init__(self, name, breed = "golden retriever")  
        self.color = color
        
    def showdetails(self):
        dog.showdetails(self)
        print(f"color: {self.color}")    
        
o = dog("tommy", "black")
o.showdetails()
print(golden_retriever.mro())                  