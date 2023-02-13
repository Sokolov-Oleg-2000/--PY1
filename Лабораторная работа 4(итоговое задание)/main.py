import doctest


class Phone:
    """ Базовый класс телефон. """

    def __init__(self, memory: int, screen: int, battery: int):
        """
        Инициализиет следующие параметры: memory, screen, battery.
        :param memory: Доступная память в телефоне в Гб.
        :param screen: Размер экрана телефона в см.
        :param battery: Объем аккумулятора в мАч
        """
        self._memory = memory
        self._screen = screen
        self._battery = battery


    def __str__(self) -> str:
        return f"Память телефона {self._memory}. Размер экрана {self._screen}. Объем батареи {self._battery}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(memory={self._memory!r}, screen={self._screen!r}, battery={self._battery!r})"

    @staticmethod
    def phone_description() -> str:
        """
        Перегружается в дочерних классах
        Прикладываем описание телефона
        """
        description = description_hello
        return description


class IOS(Phone):
    """Класс, который описывает iphone"""

    def __init__(self, memory: int, screen: int, battery: int, system: str, apple_id: int):
        """
        Инициализирует параметры: memory, screen, battery, system,apple_id
        :param memory: Доступная память в телефоне в Гб.
        :param screen: Размер экрана телефона в см.
        :param battery: Объем аккумулятора в мАч
        :param system: Название системы
        :param apple_id: Номер id телефона
        """
        super().__init__(memory, screen, battery) #вызов конструктора базового класса
        self.system = system
        self.apple_id = apple_id

    @property
    def system(self) -> str:
        return self._system

    @system.setter
    def system(self, system_ios: str):
        """Устанавливает какая система у телефона."""
        if not isinstance(system_ios, str):
            raise TypeError("Название системы должо быть типа str")
        if system_ios != 'IOS':
            raise ValueError("Не относится к данному классу, видимо у вас андроид!")
        self._system = system_ios

    @staticmethod
    def phone_description() -> str:
        """Метод из базового класса перегружается"""
        description = description_hello + description_Iphone
        return description

    @property
    def apple_id(self) -> int:
        return self._apple_id

    @apple_id.setter
    def apple_id(self, new_apple_id: int):
        """Устанавливает корректность id."""
        if not isinstance(new_apple_id, int):
            raise TypeError("Id должен быть типа int")
        if new_apple_id <= 0:
            raise ValueError("Id не может быть меньше или равен 0")
        self._apple_id = new_apple_id

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(memory={self._memory!r}, screen={self._screen!r}, battery={self._battery!r}, system={self.system!r}, apple_id={self.apple_id!r})"


class Android(Phone):
    """Класс, который описывает android"""

    def __init__(self, memory: int, screen: int, battery: int, system: str, android_id: int):
        """
        Создаем дочерний класс "Android", который будет инициализировать memory, screen, battery, system, android_id
        :param memory: Доступная память в телефоне в Гб.
        :param screen: Размер экрана телефона в см.
        :param battery: Объем аккумулятора в мАч
        :param system: Название системы
        :param android_id: Номер id телефона
        """
        super().__init__(memory, screen, battery)   #вызов конструктора базового класса
        self.system = system
        self.android_id = android_id

    @staticmethod
    def phone_description() -> str:
        """Метод из базового класса перегружается"""
        description = description_hello + description_Android
        return description

    @property
    def system(self) -> str:
        return self._system

    @system.setter
    def system(self, system_android: str):
        """Устанавливает какая система у телефона."""
        if not isinstance(system_android, str):
            raise TypeError("Название системы должо быть типа str")
        if system_android != 'Android':
            raise ValueError("Не относится к данному классу, видимо у вас iphone!")
        self._system = system_android

    @property
    def android_id(self) -> int:
        return self._android_id

    @android_id.setter
    def android_id(self, new_android_id: int):
        """Устанавливает корректность id."""
        if not isinstance(new_android_id, int):
            raise TypeError("Id должен быть типа int")
        if new_android_id <= 0:
            raise ValueError("Id не может быть меньше или равен 0")
        self._android_id = new_android_id

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(memory={self._memory!r}, screen={self._screen!r}, battery={self._battery!r}, system={self._system!r}, android_id={self._android_id!r})"

description_hello = "hello my dear friend___"
description_Iphone = "Why you choose me???"
description_Android = "Xiaomi top za svoi dengi"



if __name__ == '__main__':
    doctest.testmod()
    pass
