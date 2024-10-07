class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}'


class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color
        self.__owner = None

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if type(value) == Person:
            self.__owner = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return f'MODEL: {self.__model}, YEAR: {self.__year}, COLOR: {self.__color}'

    def drive(self):
        print(f'Car {self.__model} driving.')

    def __lt__(self, other):
        return self.__year < other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year


class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        cls.print_fuel_amount()

    @classmethod
    def print_fuel_amount(cls):
        print(f'Factory FUEL_CAR has {cls.__total_fuel} litters of fuel ({cls.get_fuel_type()}).')

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(self, FuelCar).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def __str__(self):
        return super().__str__() + f', FUEL BANK: {self.__fuel_bank}'

    def drive(self):
        print(f'Car {self.model} driving by fuel.')

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def __str__(self):
        return super().__str__() + f', BATTERY: {self.__battery}'

    def drive(self):
        print(f'Car {self.model} driving by battery.')


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


# some_car = Car('Nissan Juke', 2000, 'red')
# print(some_car)

FuelCar.buy_fuel(500)
toyota = FuelCar('Toyota Supra', 2003, 'white', 70)
print(toyota)

tesla = ElectricCar('Tesla Model X', 2022, 'red', 20000)
print(tesla)

chevrolet = HybridCar('Chevrolet Volt', 2009, 'silver', 60, 10000)
print(chevrolet)
chevrolet.drive()
print(HybridCar.mro())

number_1, number_2 = 4, 7
print(f'Number one is greater than number two: {number_1 > number_2}')
print(f'Number one is less than number two: {number_1 < number_2}')

print(f'Toyota is less in price than chevrolet: {toyota < chevrolet}')

print(number_1 + number_2)
print(toyota + chevrolet)

# FuelCar.total_fuel -= 100
FuelCar.print_fuel_amount()

my_friend = Person('Jim', 22)
toyota.owner = my_friend
tesla.owner = my_friend
# my_wife = Person('Jane', 34)
#       a = b
chevrolet.owner = Person('Jane', 34)

print(chevrolet.owner.name)