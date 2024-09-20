from counter import Counter
from classes import *
from typing import Dict, Any

class Model:
    def __init__(self, database: dict, counter: Counter) -> None:
        self._database = database
        self._counter = counter
    
    def Add(self, params: dict):
        match params['animal_type']:
            case 'Dog':
                animal = Dog(name=params['name'],
                                birthday=params['birthday'],
                                weight=params['weight'],
                                breed=params['breed'])
            case 'Cat':
                animal = Cat(name=params['name'],
                                birthday=params['birthday'],
                                weight=params['weight'],
                                breed=params['breed'])
            case 'Hamster':
                animal = Hamster(name=params['name'],
                                birthday=params['birthday'],
                                weight=params['weight'],
                                breed=params['breed'])
            case 'Horse':
                animal = Horse(name=params['name'],
                                birthday=params['birthday'],
                                weight=params['weight'],
                                carry_weight=params['carry_weight'])
            case 'Camel':
                animal = Camel(name=params['name'],
                                birthday=params['birthday'],
                                weight=params['weight'],
                                carry_weight=params['carry_weight'])
            case 'Donkey':
                animal = Donkey(name=params['name'],
                                birthday=params['birthday'],
                                weight=params['weight'],
                                carry_weight=params['carry_weight'])
        
        self._database[self._counter.counter] = animal
        self._counter.Add()


    def ShowCommands(self, target_id: int) -> list | None:
        id: int
        animal: Animal
        for id, animal in self._database.items():
            if id == target_id:
                return animal.commands
        return None
    
    def AddCommands(self, target_id: int, added_commands: list):
        id: int
        animal: Animal
        for id, animal in self._database.items():
            if id == target_id:
                start_count = final_count = len(animal.commands)
                for command in added_commands:
                    if command not in animal.commands:
                        animal.NewCommand(command)
                        final_count += 1
                return final_count - start_count
                        
    
    def Find(self, name) -> int | None:
        id: int
        animal: Animal
        for id, animal in self._database.items():
            if animal.name == name:
                return id
        return None
    
    def CanLearn(self, target_id: int):
        id: int
        animal: Animal
        for id, animal in self._database.items():
            if id == target_id:
                return False if animal.commands is None else True
