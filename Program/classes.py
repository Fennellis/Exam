import datetime


class Animal:

    def __init__(self, name: str, birthday: datetime.datetime, weight: float):
        self._name = name
        self._birthday = birthday
        self._weight = weight
        self._commands: list | None = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def birthday(self) -> datetime.datetime:
        return self._birthday

    @property
    def weight(self) -> float:
        return self._weight
    
    @property
    def commands(self) -> list | None:
        return self._commands

    def NewCommand(self, command):
        self._commands.append(command)


class Pet(Animal):
    def __init__(self, name: str, birthday: datetime, weight: float, breed: str):
        super().__init__(name, birthday, weight)
        self._breed = breed


class Dog(Pet):
    def __init__(self, name: str, birthday: datetime, weight: float, breed: str):
        super().__init__(name, birthday, weight, breed)


class Cat(Pet):
    def __init__(self, name: str, birthday: datetime, weight: float, breed: str):
        super().__init__(name, birthday, weight, breed)


class Hamster(Pet):
    def __init__(self, name: str, birthday: datetime, weight: float, breed: str):
        super().__init__(name, birthday, weight, breed)


class Pack(Animal):
    def __init__(self, name: str, birthday: datetime, weight: float, carry_weight: float):
        super().__init__(name, birthday, weight)
        self._carry_weight = carry_weight
        self._commands = None

    def NewCommand(self, command):
        raise TypeError


class Horse(Pack):
    def __init__(self, name: str, birthday: datetime, weight: float, carry_weight: float):
        super().__init__(name, birthday, weight, carry_weight)


class Camel(Pack):
    def __init__(self, name: str, birthday: datetime, weight: float, carry_weight: float):
        super().__init__(name, birthday, weight, carry_weight)


class Donkey(Pack):
    def __init__(self, name: str, birthday: datetime, weight: float, carry_weight: float):
        super().__init__(name, birthday, weight, carry_weight)
