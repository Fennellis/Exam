class Counter:
    def __init__(self) -> None:
        self._counter = 1
    
    @property
    def counter(self):
        return self._counter

    def Add(self):
        self._counter += 1