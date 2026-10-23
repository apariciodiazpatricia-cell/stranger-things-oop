from contracts.actionable import Actionable


class Character(Actionable):
    def __init__(self,name:str,age:int,health:int):
        self.name = name
        self.age=age
        self.health=health
        
    def move(self):
        print(f"👣 {self.name} is moving through Hawkins.")
              
    
    def speak(self,message:str):
        print(f"{self.name} says:'{message}'")
        
    def act(self):
        print(f"{self.name} is performing a general action")
        
    
    def __repr__(self):
        return f"🆔 [Character] Name: {self.name} | Age: {self.age} | Health: {self.health}"
    
    
    