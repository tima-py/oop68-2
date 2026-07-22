rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        return self.convert_to_kgs() + other.convert_to_kgs()

    def __sub__(self, other):
        return self.convert_to_kgs() - other.convert_to_kgs()

    def __truediv__(self, other):
        return self.convert_to_kgs() / other

    def __mul__(self, other):
        return self.convert_to_kgs() * other

    def convert_to_kgs(self):
        if self.currency != "SOM":
            return self.amount * rates[self.currency]
        return self.amount

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result = money1 + money2

print(result)