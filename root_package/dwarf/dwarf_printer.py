from root_package.weapon.weapon_printer import weapon_to_string

def dwarf_to_string(dwarf):
    return f"Dwarf: {dwarf.name}. Имеет оружие: {weapon_to_string(dwarf.weapons[0])}"        