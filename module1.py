class Hero:
    # Конструктор класса
    def __init__(self, name, hp, lvl):
        # Атрибуты экземпляра класса
        self.hero_name = name
        self.hero_hp = hp
        self.hero_lvl = lvl

    # Метод класса
    def base_action(self):
        return f"thi base action {self.hero_name}"