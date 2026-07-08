import random

class Hero:
    def __init__(self, name, hp, lvl, strength):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.strength = strength
    def greet(self):
        return f'Привет, я {self.name}, мой уровень {self.lvl}'
    def attack(self):
        self.strength -= 1
        return f'{self.name} наносит удар!'
    def rest(self):
        self.hp += 1
        return f'{self.name} отдыхает...'


class Warrior(Hero):
    def __init__(self, name, hp, lvl, strength, stamina):
        super().__init__(name, hp, lvl, strength)
        self.stamina = stamina

    def attack(self):
        self.strength -= 1
        return f'{self.name} атакует мечом!'


class Mage(Hero):
    def __init__(self, name, hp, lvl, strength, mana):
        super().__init__(name, hp, lvl, strength)
        self.mana = mana

    def attack(self):
        self.strength -= 1
        return f'{self.name} кастует заклинание!'


class Assassin(Hero):
    def __init__(self, name, hp, lvl, strength, stealth):
        super().__init__(name, hp, lvl, strength)
        self.stealth = stealth

    def attack(self):
        self.strength -= 1
        return f'{self.name} атакует из-под тишка!'

warrior = Warrior('Warrior', 100, 100, 100, 100)
mage = Warrior('Mage', 100, 100, 100, 20)
assassin = Warrior('Assassin', 100, 100, 100, 100)

print(warrior.attack())
print(mage.attack())
print(assassin.attack())

heroes = ['Warrior', 'Mage', 'Assassin']

print('===========================================')
print('🎮 Мини-игра "Камень, Ножницы, Бумага"\n'
      'Соответствие героев:\n'
      'Warrior  = Камень\n'
      'Assassin = Ножницы\n'
      'Mage     = Бумага')
print('===========================================')
while True:
    hero = input('Warrior / Mage / Assassin\nВыберите героя: ')
    opponent = random.choice(heroes)

    print('===========================================')
    if hero in heroes:
        print(f'Вы выбрали: {hero}')
    else:
        print('Выберайте героя только из Warrior / Mage / Assassin!!')
        continue

    print(f'Противник: {opponent}')

    if hero == opponent:
        print('Ничья')

    elif (hero == 'Warrior' and opponent == 'Assassin') or (hero == 'Assassin' and opponent == 'Warrior'):
        print('Воин победил Ассассина!')

    elif (hero == 'Assassin' and opponent == 'Mage') or (hero == 'Mage' and opponent == 'Assassin'):
        print('Ассасин побеждает Мага!')

    elif (hero == 'Mage' and opponent == 'Warrior') or (hero == 'Warrior' and opponent == 'Mage'):
        print('Маг побеждает Воина!')
    print('===========================================')