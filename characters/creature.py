from characters.character import Character


class UpsideDownCreature(Character):
    def __init__(self, name:str, health: int, origin_dimension: str, weakness: str):
        super().__init__(name, 0, health)
        self.origin_dimension = origin_dimension
        self.weakness = weakness
        
    def roar(self):
        print(f"{self.name} roars into the darkness of {self.origin_dimension}!")
        

class Demogorgon(UpsideDownCreature):
    def __init__(self, name: str, health: int, origin_dimension: str, weakness:str, growth_stage:str):
        super().__init__(name,health,origin_dimension,weakness)
        self.growth_stage=growth_stage
        
    def act (self):
        print (f"{self.name} ({self.growth_stage}) leaps from the shadows and strikes!")
    
    def open_portal(self):
        print(f"{self.name} tears open an interdimensional gate into hawkins.")
        
class Vecna(UpsideDownCreature):
    def __init__(self, name:str, health:int, origin_dimension:str, weakness:str, current_victim: str, fatal_song: str):
         super().__init__(name,health,origin_dimension,weakness)
         self.current_victim=current_victim
         self.fatal_song=fatal_song
         
    
    def act(self):
        print(f"{self.name} invades the mind of {self.current_victim} as they hear {self.fatal_song}")
        
    def curse_victim(self):
        print(f"{self.name} begins to levitate {self.current_victim}")
        
    
    

        

        