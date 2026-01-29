# 5.1 
class Dwarf:
    def __init__(self, name, age, weapons):
        self.__name = name
        self.__age = age
        self.__health = 100
        self.__weapons = weapons
        self.__current_weapon_num = 0
        
    def Fight(self, enemy):
        weapon = self.__weapons[self.__current_weapon_num]
        weapon.Hit(enemy)
        
    def Take_damage(self, damage):
        self.__health -= damage
        
    def Rest(self, hours):
        self.__health += hours
        
    def Change_weapon(self):
        if self.__current_weapon_num == len(self.__weapons):
            self.__current_weapon_num = 0
        else: self.__current_weapon_num +=1
        
class Weapon:
    def __init__(self, attack_type, name, damage):
        self.__attack_type = attack_type #1 - режущее, 2-тупое
        self.__name = name
        self.__damage = damage
        
    def Hit(self, enemy):
        enemy.health -= self.__damage
        
    def Break(self):
        self.__damage = 0
        
    def Rust(self):
        self.__damage = self.__damage / 2
        
class Animal:
    def __init__(self, name, mass, kind, biome, speed):
        self.__name = name
        self.__mass = mass
        self.__kind = kind
        self.__energy = 100
        self.__speed = speed
        
    def Eat(self, meal):
        self.__mass += meal / 10
        
    def Sleep(self):
        self.__energy = 100
        
    def Run(self, hours):
        self.__energy -= hours * self.__speed
        self.__mass -= hours * self.__speed / 100

######################
# 5.2

class Device:
    def __init__(self):
        self.__on = False
    def turn_on(self):
        self.__on = True
    def turn_off(self):
        self.__on = False
        
class Laptop(Device):
    def run_Java(self):
        print('Java program')
    def run_python(self):
        print('Python program')
        
class Phone(Device):
    def call(self, contact):
        print('Calling ' + contact)
    def message(self, message):
        print('Sending message: ' + message)
        
class Employee:
    def __init__(self):
        self._energy = 100
        
    def think(self, minutes):
        self._energy -= minutes

    def drink_coffee(self):
        self._energy += 10
        
class Programmer(Employee):

    def __init__(self):
        self.__lines = 0
        self.__tests = 0
        
    def write_code(self, hours):
        self.__lines += 5
        
    def write_test(self, hours):
        self.__tests += 1
        
class Analist(Employee):
    
    def __init__(self):
        self.__pages = 0
        self.__reports = 0
        
    def write_documentation(self):
        self.__lines += 1
        
    def prepare_report(self):
        self.__tests += 1
