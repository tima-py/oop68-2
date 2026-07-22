from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, hp, lvl, strength):
        self.name = name
        self.__hp = hp
        self.lvl = lvl
        self.strength = strength

    def greet(self):
        return f'Привет, я {self.name}, мой уровень {self.lvl}'

    @abstractmethod
    def attack(self):
        pass

    def rest(self):
        self.__hp += 1
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
mage = Mage('Mage', 100, 100, 100, 20)
assassin = Assassin('Assassin', 100, 100, 100, 100)

print(warrior.greet())
print(warrior.attack())
print(warrior.rest())

print(mage.greet())
print(mage.attack())
print(mage.rest())

print(assassin.greet())
print(assassin.attack())
print(assassin.rest())