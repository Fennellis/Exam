from model import Model
from view import View
from counter import Counter
from controller import Controller

ctrl = Controller(Model(dict(), Counter()), View())
ctrl.Start()
