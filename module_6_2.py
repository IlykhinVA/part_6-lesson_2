class Vehicle:
    __COLOR_VARIANTS = ['голубой', 'красный', 'зеленый', 'чёрный', 'белый']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner =owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return str(f'Модель: {self.__model},')

    def get_horsepower(self):
        return str(f'Мощность двигателя: {self.__engine_power} л.с.,')

    def get_color(self):
        return str(f'Цвет: {self.__color},')

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), 'Владелец:', self.owner)

    def set_color(self, new_color):
        # self.color=new_color

        for i in range(len(self.__COLOR_VARIANTS)):
            if str(new_color).lower() == self.__COLOR_VARIANTS[i]:
                self.__color = (new_color.lower())
                return
        print(f'Нельзя сменить цвет на {(new_color.lower())}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Кот Матроскин', 'Toyota Mark II', 'белый', 500)
vehicle1.print_info()
vehicle1.set_color('Синий')
vehicle1.set_color('КРАСНЫЙ')
vehicle1.owner = 'Дядя Фёдор'
vehicle1.print_info()

