class Dwarf:
    def  __init__(self, name, age, weapons):
        self.name = name
        self.age = age
        self.health = 100
        self.weapons = weapons
        self.current_weapon_num = 0

    def Fight(self, enemy):
        weapon = self.weapons[self.current_weapon_num]
        weapon.Hit(enemy)

    def Take_damage(self, damage):
        health -= damage

    def Rest(self, hours):
        health += hours

    def Change_weapon(self):
        if self.current_weapon_num == len(weapons):
            self.current_weapon_num = 0
        else: self.current_weapon_num +=1

class Weapon:

    def __init__(self, attack_type, name, damage):
        self.attack_type = attack_type #1 - режущее, 2-тупое
        self.name = name
        self.damage = damage

    def Hit(self, enemy):
        enemy.health -= self.damage

    def Break(self):
        self.damage = 0

    def Rust(self):
        self.damage = self.damage / 2


class Animal:

    def __init__(self, name, mass, kind, biome, speed):
        self.name = name
        self.mass = mass
        self.kind = kind
        self.energy = 100
        self.speed = speed

    def Eat(self, meal):
        self.mass += meal / 10

    def Sleep(self):
        self.energy = 100

    def Run(self, hours):
        self.energy -= hours * speed
        self.mass -= hours * speed / 100


sword = Weapon('sword', 1, 10)
axe = Weapon('axe', 1, 5)

torin = Dwarf('Torin', 210, [sword])
bubin = Dwarf('Bubin', 150, [axe])

bubin.Fight(torin)
print('Torin health after attack: ' + str(torin.health)) # 95
torin.Fight(bubin)
print('Bubin health after attack: ' +  str(bubin.health)) # 90




