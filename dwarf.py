# 2. Классы из компьютерной игры.

class Dwarf:
    name = ''
    age = 0
    health = 100
    weapons = []

class Weapon:
    attack_type = ''
    name = ''
    damage = 0 # сколько урона наносит

class Animal:
    name = ''
    age = 0
    type = []
    biome = []


snake = Animal()
snake.name = 'snake'
snake.age = 2
snake.type = 'poisonous'
snake.biome = ['forest', 'meadow']

sword = Weapon()
sword.name = 'sword'
sword.attack_type = 'edged'
sword.damage = 10

whip = Weapon()
whip.name = 'whip'
whip.attack_type = 'blunt'
whip.damage = 5

torin_dwarf = Dwarf()
torin_dwarf.name = 'Torin'
torin_dwarf.age = 100
torin_dwarf.skills = ['warrior']
torin_dwarf.weapons = [sword, whip]


print(torin_dwarf.name)
print(torin_dwarf.age)
print(torin_dwarf.skills)
print(sword.name)
print(sword.attack_type)
print(whip.name)
print(whip.attack_type)
print(snake.name)
print(snake.biome)


# 3. Эффект от передачи по ссылке.
# Поменяли название у первого оружия из арсенала Торина, и у меча изменилось название.
weapon = torin_dwarf.weapons[0]
weapon.name = 'axe'

print(sword.name) #axe
