# Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.

player_name = input('enter player name')
player = {'name':player_name, 'health':100, 'damage':50, 'armor':1.2}

enemy_name = input('enter enemy name')
enemy = {'name':enemy_name, 'health':50, 'damage':30, 'armor':1.5}

def get_damage(damage, armor): # рассчет урона в зависимости от брони
    return damage/armor

def attack(unit,target): # вычитаем из здоровья урон с четом брони из функции выше
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)