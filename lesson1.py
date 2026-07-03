# HeroMage
# hero_mage
class Hero:
    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты экземпляра класса
        self.name = name
        self.hp = hp
        self.lvl = lvl


# Объект | Экземпляр класса
kirito = Hero('Kirito', 1000, 100)
asuna = Hero('Asuna', 1000, 100)

print(kirito.name)
print(asuna.name)
