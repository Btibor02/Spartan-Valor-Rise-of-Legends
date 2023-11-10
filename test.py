import equipments

INVENTORY = [equipments.Weapons.Kolós(), equipments.Shields.AspisOfHoplon(), equipments.Potions.Heal(), equipments.Potions.Shield()]
print(f'Weapon = {INVENTORY[0][0]}')

INVENTORY[0] = equipments.Weapons.Dory()
print(f'Weapon = {INVENTORY[0][0]}')