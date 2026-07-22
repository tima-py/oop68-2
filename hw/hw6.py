from faker import Faker # Эта библиотека нужна для генерирования данных
from colorama import Fore, Back, Style # Эта библиотека нужна для изменения цвета текста в консоли

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Fore.YELLOW + Back.RESET + 'some yellow text')
print(Back.BLACK + 'and with a black background')
# print(Style.RESET_ALL)
# print('back to normal now')

fake_en = Faker('en_US')
fake_ru = Faker('ru_RU')

print(f"EN: {fake_en.name()}")
print(f"RU: {fake_ru.name()}")