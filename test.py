import equipment

INVENTORY = [equipment.Weapons.Kolós(), equipment.Shields.AspisOfHoplon(), equipment.Potions.Heal(), equipment.Potions.Shield()]
print(f'Weapon = {INVENTORY[0][0]}')

INVENTORY[0] = equipment.Weapons.Dory()
print(f'Weapon = {INVENTORY[0][0]}')