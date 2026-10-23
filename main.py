from characters.human import PoweredHuman, NormalHuman
from characters.creature import Demogorgon, Vecna
from services.battle_simulator import BattleSimulator

def main():
    print("👾 Welcome to Hawkins Initializing Party...👾\n")
    
    eleven= PoweredHuman("Eleven", 14, 100, "Mind", "Telekinesis", 95)
    dustin= NormalHuman("Dustin", 14, 100, "Walkie Cerebro", "Cap", "Bicycle")
    steve= NormalHuman("Steve Harrington", 19, 100, "Spiked Bat", "Hairspray","BMW2")
    dart= Demogorgon("Dart", 80, "Upside Down", "Fire", "Demodog")
    vecna= Vecna("Henry Creel", 500, "Upside Down","Kate Bush Music", "Max", "Running up That Hill") 
    
    steve.speak("Keep calm Kids, I'm taking care of this.")
    dustin.use_item()
    dart.open_portal()
    
    
    hawkins_party=[eleven,dustin,steve,dart,vecna]
    BattleSimulator.run_simulation(hawkins_party)
    
    
if __name__=="__main__":
    main()