def damage(skill1, skill2):
    damage1 = skill1 + 10
    damage2 = skill2 * 3
    print(type(skill1))
    print(type(skill2))
    return damage1, damage2


skill_1 = int(input())
skill_2 = int(input())

damage_skill1, damage_skill2 = damage(skill1=skill_1, skill2=skill_2)

print(damage_skill1, damage_skill2)
damage(1, 2)
