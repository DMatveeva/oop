from root_package.dwarf.dwarf_printer import dwarf_to_string
import datetime


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

print(f"Текущая дата: {datetime.datetime.now()}")
print(f"Текущее время: {datetime.datetime.now().time()}")

sword = Weapon(1, 'Меч', 10)
axe = Weapon(1, 'Топор', 5)

bilbo = Dwarf('Бильбо', 210, [sword])
goblin = Dwarf('Гоблин', 150, [axe])

print(dwarf_to_string(bilbo))
print(dwarf_to_string(goblin))
