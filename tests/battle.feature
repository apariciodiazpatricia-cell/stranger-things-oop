Feature: Simulación de batalla en Hawkins (Stranger Things POO)
  Como desarrollador de software
  Quiero modelar las entidades de Hawkins y el Upside Down
  Para validar su comportamiento polimórfico en combate

  # --- 1. ELEVEN (POWERED HUMAN) ---
  Scenario: Eleven usa su poder telequinético y sufre desgaste psíquico
    Given que Eleven tiene 95 puntos de energía
    When Eleven ejecuta su acción de combate
    Then su energía debe reducirse a 75 puntos
    And debe sangrarle la nariz por el esfuerzo psíquico

  # --- 2. DUSTIN (NORMAL HUMAN) ---
  Scenario: Dustin coordina al grupo usando su equipamiento
    Given que Dustin está equipado con "Walkie Cerebro" y "Cap"
    When Dustin ejecuta su acción de combate
    Then debe transmitir órdenes usando su arma "Walkie Cerebro"
    And su movilidad debe estar ligada a su bicicleta

  # --- 3. STEVE HARRINGTON (NORMAL HUMAN) ---
  Scenario: Steve defiende a los chicos con su bate con clavos
    Given que Steve Harrington tiene equipado "Spiked Bat"
    And conduce su vehículo "BMW"
    When Steve ejecuta su acción de combate
    Then debe golpear firmemente a los enemigos usando "Spiked Bat"

  # --- 4. DART (DEMOGORGON / DEMODOG) ---
  Scenario: Dart ataca desde las sombras como Demodog
    Given que Dart pertenece a la dimensión "Upside Down"
    And su fase de crecimiento es "Demodog"
    When Dart ejecuta su acción de combate
    Then debe abalanzarse desde las sombras abriendo sus pétalos

  # --- 5. VECNA (UPSIDE DOWN BOSS) ---
  Scenario: Vecna inicia una maldición sobre su víctima actual
    Given que Vecna acecha desde el Upside Down
    And su víctima actual es "Max"
    When Vecna ejecuta su acción
    Then debe invadir la mente de Max
    And la salvación debe requerir reproducir "Running Up That Hill"

  # --- 6. POLIMORFISMO COLECTIVO ---
  Scenario: Ejecución polimórfica del turno grupal en el simulador
    Given una party formada por Eleven, Dustin, Steve, Dart y Vecna
    When el BattleSimulator ejecuta el turno de todos los integrantes
    Then todas las entidades deben ejecutar act() sin violar el contrato Actionable