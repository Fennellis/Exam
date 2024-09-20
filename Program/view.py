from datetime import datetime

class View:
    def __init__(self) -> None:
        pass

    def Menu(self):
        text = """
Главное меню:
1. Завести новое животное
2. Посмотреть список команд животного
3. Обучить животное новым командам
4. Выход   
        """
        print(text)
        return int(input('Введите команду: '))

    def NewAnimal(self):
        params = dict()

        name = input('Введите имя животного: ')
        if not name.isalpha():
            print('Неверное имя животного.')
            return
        else:
            params['name'] = name.capitalize()

        birthday = input('Введите дату рождения животного (день/месяц/год): ')
        try:
            birthday = datetime.strptime(birthday, "%d/%m/%Y").date()
        except ValueError:
            print('Неверный формат даты')
            return
        params['birthday'] = birthday

        try:
            weight = int(input('Введите вес животного: '))
            if weight < 0:
                raise ValueError
            params['weight'] = weight
        except ValueError:
            print('Неверный вес животного.')
            return

        animal_type = int()
        text = """
Доступные виды:
1. Собака
2. Кошка
3. Хомяк
4. Лошадь
5. Верблюд
6. Осёл
        """
        print(text)

        try:
            animal_type = int(input('Выберите тип животного: '))
            if animal_type not in range(1, 6 + 1):
                raise ValueError
        except ValueError:
            print('Неверный тип животного.')
            return

        if animal_type in range(1, 3 + 1):
            match animal_type:
                case 1:
                    animal_type = 'Dog'
                case 2:
                    animal_type = 'Cat'
                case 3:
                    animal_type = 'Humster'
            
            breed = input('Введите породу животного: ')
            if not breed.isalpha():
                print('Неверная порода животного.')
                return
            
            params['breed'] = breed
            
        if animal_type in range(4, 6 + 1):
            match animal_type:
                case 4:
                    animal_type = 'Horse'
                case 5:
                    animal_type = 'Camel'
                case 6:
                    animal_type = 'Donkey'
            
            carry_weight = input('Введите грузоподъемность животного: ')
            try:
                carry_weight = int(carry_weight)
            except ValueError:
                print('Неверная порода животного.')
                return
            
            params['carry_weight'] = carry_weight
        
        params['animal_type'] = animal_type

        return params

    def ShowCommand(self, commands: list | None):
        if commands == None:
            print('Животное не способно выполнять команды.')
        elif len(commands) == 0:
            print('Животное еще не знает команд.')
        else:
            print('Список команд животного:')
            i = 1
            for command in commands:
                print(f'{i}. {command}')
                i += 1
    
    def LearnCommand(self, can_learn: bool) -> list | None:
        if can_learn:
            commands = []
            while True:
                command = input('Введите команду (оставьте пустым для выхода): ')

                if command == '':
                    break
                else:
                    commands.append(command)
            return commands
        
        else:
            print('Животное не способно обучаться.')
            return None
    
    def SuccessfulAddition(self, count: int):
        print(f'{count} команд успешно добавлены.')
            
    def FindAnimal(self):
        return input('Введите имя животного: ')
    
    def NotFound(self):
        return print('Животное с таким именем не обнаружено.')
    