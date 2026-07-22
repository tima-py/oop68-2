# HeroMage
# hero_mage
class Hero:
    # Конструктор класса
    def __init__(self, name, hp, lvl, strength):
        # Атрибуты экземпляра класса
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


# Объект | Экземпляр класса
kirito = Hero('Kirito', 1000, 100, 50)
asuna = Hero('Asuna', 1000, 100, 40)

print('-------------------')
print(kirito.name)
print(kirito.greet())
print(kirito.attack())
print(kirito.strength)
print(kirito.rest())
print(kirito.hp)
print('-------------------')

print('-------------------')
print(asuna.name)
print(asuna.greet())
print(asuna.attack())
print(asuna.strength)
print(asuna.rest())
print(asuna.hp)
print('-------------------')