import unittest
from characters.human import PoweredHuman, NormalHuman
from characters.creature import Demogorgon, Vecna
from contracts.actionable import Actionable
from services.battle_simulator import BattleSimulator


class TestStrangerThingsOOP(unittest.TestCase):

    def setUp(self):
        """
        GIVEN común: Instanciamos a todos los personajes de Hawkins
        con sus atributos iniciales.
        """
        self.eleven = PoweredHuman("Eleven", 14, 100, "Mind", "Telekinesis", 95)
        self.dustin = NormalHuman("Dustin", 14, 100, "Walkie Cerebro", "Cap", "Bicycle")
        self.steve = NormalHuman("Steve Harrington", 19, 100, "Spiked Bat", "Hairspray", "BMW")
        self.dart = Demogorgon("Dart", 80, "Upside Down", "Fire", "Demodog")
        self.vecna = Vecna("Henry Creel", 500, "Upside Down", "Kate Bush Music", "Max", "Running Up That Hill")

    # --- ESCENARIO 1: ELEVEN ---
    def test_scenario_01_eleven_telekinesis_and_energy_drain(self):
        # Given: Guardamos la energía inicial
        initial_energy = self.eleven.energy_level

        # When: Ejecuta su acción
        self.eleven.act()

        # Then: La energía se reduce (funciona con -20, con -10 o cualquier gasto)
        self.assertLess(self.eleven.energy_level, initial_energy)
        self.assertEqual(self.eleven.power_type, "Telekinesis")

    # --- ESCENARIO 2: DUSTIN ---
    def test_scenario_02_dustin_equipment_and_mobility(self):
        # Given & Then: Dustin posee su walkie Cerebro, gorra y bicicleta
        self.assertEqual(self.dustin.weapon, "Walkie Cerebro")
        self.assertEqual(self.dustin.key_item, "Cap")
        self.assertEqual(self.dustin.vehicle, "Bicycle")  # Corregido: vehicle
        
        # Ejecutamos sus métodos
        self.dustin.act()
        self.dustin.pedal()     # Ejecutamos pedal()
        self.dustin.use_item()  # Ejecutamos use_item()

    # --- ESCENARIO 3: STEVE HARRINGTON ---
    def test_scenario_03_steve_combat_and_vehicle(self):
        # Given & Then: Steve está armado con su bate con clavos y su BMW
        self.assertEqual(self.steve.weapon, "Spiked Bat")
        self.assertEqual(self.steve.key_item, "Hairspray")
        self.assertEqual(self.steve.vehicle, "BMW")  # Corregido: vehicle
        
        # Ejecutamos los métodos heredados de Human
        self.steve.act()
        self.steve.attack()  # Ejecutamos attack()
        self.steve.flee()    # Ejecutamos flee()

    # --- ESCENARIO 4: DART (DEMOGORGON) ---
    def test_scenario_04_dart_creature_properties(self):
        # Given & Then: Dart pertenece al Upside Down y está en etapa Demodog
        self.assertEqual(self.dart.origin_dimension, "Upside Down")
        self.assertEqual(self.dart.weakness, "Fire")
        self.assertEqual(self.dart.growth_stage, "Demodog")
        
        # Ejecutamos sus métodos
        self.dart.act()
        self.dart.roar()         # Ejecutamos roar()
        self.dart.open_portal()  # Ejecutamos open_portal()

    # --- ESCENARIO 5: VECNA (BOSS) ---
    def test_scenario_05_vecna_curse_and_counter_song(self):
        # Given & Then: Vecna acecha a Max y su talón de Aquiles es Kate Bush
        self.assertEqual(self.vecna.current_victim, "Max")
        self.assertEqual(self.vecna.fatal_song, "Running Up That Hill")
        self.assertEqual(self.vecna.health, 500)
        
        # Ejecutamos sus métodos
        self.vecna.act()
        self.vecna.curse_victim()  # Ejecutamos curse_victim()

    # --- ESCENARIO 6: POLIMORFISMO Y SIMULADOR ---
    def test_scenario_06_polymorphic_battle_round(self):
        party = [self.eleven, self.dustin, self.steve, self.dart, self.vecna]

        for character in party:
            self.assertIsInstance(character, Actionable)

        try:
            BattleSimulator.run_simulation(party)
            simulation_passed = True
        except Exception:
            simulation_passed = False

        self.assertTrue(simulation_passed)


if __name__ == "__main__":
    unittest.main()