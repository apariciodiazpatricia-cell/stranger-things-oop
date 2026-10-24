from characters.character import Character

class Human(Character):
    def __init__(self, name: str, age: int, health: int, weapon: str = None):
        super().__init__(name, age, health)
        self.weapon = weapon
        
    def flee(self):
        print(f"{self.name}is running away to safety!")
        
    def attack(self):
        print(f"{self.name} attacks using {self.weapon}!")
        
        
class PoweredHuman(Human):
    def __init__(self, name: str, age: int, health: int, weapon: str , power_type: str, energy_level: int):
        
        super().__init__(name, age, health, weapon)
        self.power_type=power_type
        self.energy_level=energy_level
        
    def act(self):
        if self.energy_level>=20:
            self.energy_level-=20
            print(f"{self.name} uses {self.power_type}! Energy remaining: {self.energy_level}%")
            self.bleed_nose()
        else:
            print(f"{self.name} is exhausted and needs rest!")
    def bleed_nose(self):
        print(f"🩸 {self.name}'s nose starts bleeding due to psychic strain.")
        
class NormalHuman(Human):
    def __init__(self, name: str,age: int, health: int, weapon: str, key_item: str, vehicle: str):
        super().__init__(name,age,health,weapon)
        self.key_item=key_item
        self.vehicle=vehicle
        
    def act(self):
        print(f"{self.name} strikes firmly using {self.weapon}!")
        
    def use_item(self):
        print(f"{self.name} uses {self.key_item} to coordinate.")
    
    def pedal(self):
        print(f" {self.name} speeds away on their {self.vehicle}!")
        
        
            
            
        
    
        
        
        
    
    