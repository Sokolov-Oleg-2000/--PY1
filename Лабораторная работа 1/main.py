import doctest


class Balloon:
    def __init__(self, percent_helium: float, percent_nitrogen: float):
        """
        Создание и подготовка к работе объекта "Шарик"
        :param percent_helium: Процентное содержание гелия в объеме шарика
        :param percent_nitrogen: Процентное содержание азота в объеме шарика
        Примеры:
        >>> balloon = Balloon(50, 50)  # инициализация экземпляра класса
        """
        if not isinstance(percent_helium, (int, float)):
            raise TypeError("Процентное содержание гелия в шарике должно быть типа int или float")
        if percent_helium > 100:
            raise ValueError("Процентное содержание гелия в шарике не может быть больше 100!")
        self.percent_helium = percent_helium

        if not isinstance(percent_nitrogen, (int, float)):
            raise TypeError("Процентное содержание азота в шарике должно быть типа int или float")
        if percent_nitrogen > (100-percent_helium):
            raise ValueError("Процентное содержание азота и гелия в сумме не может превышать 100!")
        self.percent_nitrogen = percent_nitrogen

    def is_balloon_fly(self) -> bool:
        """
        Функция которая проверяет будет ли шарик летать
        :return: Будет ли шарик летать
        Примеры:
        >>> balloon = Balloon(90, 10)
        >>> balloon.is_balloon_fly()
        """
        ...

    def add_helium_to_balloon(self, helium: float) -> None:
        """
        Добавление процентного соотношения гелия в шарике.
        :param helium: на сколько процентов увеличим гелий и уменьшим азот
        :raise ValueError: Если процентное соотношение гелия превышает 100 то вызываем ошибку
        Примеры:
        >>> balloon = Balloon(20, 80)
        >>> balloon.add_helium_to_balloon(20)
        """
        if not isinstance(helium, (int, float)):
            raise TypeError("Добавляемый гелий должен быть типа int или float")
        if helium < 0:
            raise ValueError("Добавляемые проценты гелия должны быть положительными")
        ...

    def drop_helium_from_balloon(self, helium1: float) -> None:
        """
        Уменьшение процентного соотношения гелия.
        :param helium1: на сколько процентов уменьшим гелий и увеличим азот
        :raise ValueError: Если  уменьшаем на больший процент гелия, чем имеется,
        то возвращается ошибка.
        :return: Получившееся процентное соотношение после уменьшения гелия.
        Примеры:
        >>> balloon = Balloon(50, 50)
        >>> balloon.drop_helium_from_balloon(10)
        """
        ...


class Water:
    def __init__(self, pressure: float, temperature: float):
        """
        Создание и подготовка к работе объекта "Вода"
        :param pressure: Давление
        :param temperature: Температура
        Примеры:
        >>> water = Water(760, 100)  # инициализация экземпляра класса
        """
        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление должно быть типа int или float")
        if pressure <= 641:
            raise ValueError("Вы покинули планету Земля??? Очень низкое давление!")
        self.pressure = pressure

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура воды должна быть int или float")
        if temperature < 0:
            raise ValueError("При таких температурах вода превращается в лёд")
        self.temperature = temperature

    def is_water_boiling(self) -> bool:
        """
        Функция которая проверяет закипит ли вода
        :return: Закипит ли вода
        Примеры:
        >>> water = Water(760, 100)
        >>> water.is_water_boiling()
        """
        ...

    def lower_temperature_to_water(self, water_temperature_low: float) -> None:
        """
        Понижение температуры воды.
        :param water_temperature_low: Количество градуов Цельсия, на которое мы понижаем температуру воды
        :raise ValueError: Если итоговая температура ниже 0, то вызываем ошибку
        Примеры:
        >>> water = Water(700, 70)
        >>> water.lower_temperature_to_water(28)
        """
        if not isinstance(water_temperature_low, (int, float)):
            raise TypeError("При понижении температуры она должна быть типа int или float")
        if water_temperature_low < 0:
            raise ValueError("Значение, на которое мы понижаем температуру воды должно быть положительным числом")
        ...


class Student:
    def __init__(self, entrant_age: int, entrant_iq_test: float, entrant_average_score: float):
        """
        Создание и подготовка к работе объекта "Студент"
        :param entrant_age: Возраст абитуриента
        :param entrant_iq_test: Баллы абитуриента за IQ тест
        :param entrant_average_score: Средний балл абитуриента
        Примеры:
        >>> student = Student(18, 120, 5)  # инициализация экземпляра класса
        """
        if not isinstance(entrant_age, int):
            raise TypeError("Возраст студента должен быть типа int")
        if entrant_age <= 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.entrant_age = entrant_age

        if not isinstance(entrant_iq_test, (int, float)):
            raise TypeError("Количество баллов за IQ тест должно быть int или float")
        if entrant_iq_test < 0:
            raise ValueError("Количество баллов за IQ тест не может быть отрицательным")
        self.entrant_iq_test = entrant_iq_test

        if not isinstance(entrant_average_score, (int, float)):
            raise TypeError("Средний балл должен быть int или float")
        if entrant_average_score < 0:
            raise ValueError("Средний балл не может быть отрицательным")
        self.entrant_average_score = entrant_average_score

    def is_age_appropriate(self) -> bool:
        """
        Функция которая проверяет подходит ли абитуриент по возрасту
        :return: Подходит ли абитуриент по возрасту
        Примеры:
        >>> student = Student(18, 120, 4)
        >>> student.is_age_appropriate()
        """
        ...

    def add_extra_scores(self, scores: float) -> None:
        """
        Добавление баллов к тесту IQ за дополнительные заслуги.
        :param scores: Количество дополнительных баллов
        :raise ValueError: Если количество дополнительных баллов превышает 20, то вызываем ошибку
        Примеры:
        >>> student = Student(17, 100, 3)
        >>> student.add_extra_scores(18)
        """
        if not isinstance(scores, (int, float)):
            raise TypeError("Дополнительные баллы должны быть типа int или float")
        if scores < 0:
            raise ValueError("Добавляемые баллы должны быть в виде положительного числа")
        if scores > 20:
            raise ValueError("Нельзя добавить более 20 баллов")
        ...

    def is_it_student(self) -> bool:
        """
        Функция которая проверяет подходит ли абитуриент по всем трем параметрам
        :return: Подходит ли абитуриент по iq, среднему баллу и возрасту
        Примеры:
        >>> student = Student(18, 120, 5)
        >>> student.is_it_student()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
