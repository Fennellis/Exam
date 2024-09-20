from model import Model
from view import View
from classes import *

class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self._m = model
        self._v = view
    
    def Start(self):
        while True:
            match self._v.Menu():
                case 1:
                    params = self._v.NewAnimal()
                    if params == None:
                        continue
                    self._m.Add(params)
                case 2:
                    id = self._m.Find(self._v.FindAnimal())
                    if id is None:
                        self._v.NotFound()
                        continue
                    self._v.ShowCommand(self._m.ShowCommands(id))
                case 3:
                    id = self._m.Find(self._v.FindAnimal())
                    if id is None:
                        self._v.NotFound()
                        continue
                    commands = self._v.LearnCommand(self._m.CanLearn(id))
                    if commands is not None:
                        added_commands: int = self._m.AddCommands(id, commands)
                        self._v.SuccessfulAddition(added_commands)
                case 4:
                    return