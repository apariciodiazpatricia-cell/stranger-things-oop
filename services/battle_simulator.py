import time
from characters.human import Human
from characters.creature import UpsideDownCreature

class BattleSimulator:
    @staticmethod
    def run_simulation(characters:list):
        print ("\n"+"=" * 45)
        print("⚡THE BATTLE OF HAWKINS BEGINS⚡")
        print("="*45 +"\n")   
        
        for character in characters:
            print(f"👉 Turn of {character.name}(Health: {character.health})")
            character.move()
            character.act()
            print("-"*35)
            time.sleep(1.2)
            
        
        