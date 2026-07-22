class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} готов к бою!'


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    bank_name = 'Simba'

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero).__name__ == type(other.hero).__name__:
            return self.balance + other.balance
        return 'Ошибка: Нельзя сложить счета героев разных классов!'

    def __eq__(self, other):
        if type(self.hero).__name__ == type(other.hero).__name__ and self.hero.lvl == other.hero.lvl:
            return True
        return False

    @property
    def balance(self):
        return self._balance

    def login(self, password):
        if password == self.__password:
            return True
        return False

    def full_info(self):
        return f'{self.hero}, {self._balance}'

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

merlin_mage = MageHero('Merlin', 50, 100, 150)
conan_warrior = WarriorHero('Conan', 50, 100, 150)
acc1 = BankAccount(merlin_mage, 5000, 1234)
acc2 = BankAccount(merlin_mage, 3000, 1234)
acc3 = BankAccount(conan_warrior, 4000, 1234)

print(merlin_mage.action())
print(conan_warrior.action())
print(acc1.__str__())
print(acc2.__str__())
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

print("Сумма мага и воина:", acc1 + acc3)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

# ✅ Итоговый вывод программы
#
# Маг Merlin кастует заклинание! MP: 150
# Воин Conan рубит мечом! Уровень: 50
# Merlin | Баланс: 5000 SOM
# Merlin | Баланс: 3000 SOM
# Банк: Simba
# Бонус за уровень: 500 SOM
#
# Сумма счетов двух магов: 8000
# Ошибка: Нельзя сложить счета героев разных классов!
#
# Mage1 == Mage2 ? True
# Mage1 == Warrior ? False
