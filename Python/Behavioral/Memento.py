class Memento(object):
    def __init__(self, strState):
        self._state = strState

    def getState(self):
        return self._state

class Originator(object):
    def __init__(self):
        self.setState("")

    def setState(self, strState):
        self._state = strState

    def getState(self):
        return self._state

    def saveStateToMemento(self):
        return Memento(self._state)

    def getStateFromMemento(self, inMemento):
        self._state = inMemento.getState()


class CareTaker(object):
    def __init__(self):
        self._mementoList = []

    def add(self, inMemento):
        self._mementoList.append(inMemento)

    def undo(self):
        if not self._mementoList:
            return
        return self._mementoList.pop(-1)


class Editor(object):
    def __init__(self):
        self.originator = Originator()
        self.careTaker = CareTaker()

    def __str__(self):
        return self.originator.getState()

    def typeStr(self, type_str):
        self.careTaker.add(self.originator.saveStateToMemento())
        self.originator.setState(self.originator.getState() + type_str)

    def replaceStr(self, type_str):
        self.careTaker.add(self.originator.saveStateToMemento())
        self.originator.setState(type_str)

    def undo(self):
        memento = self.careTaker.undo()
        if memento:
            self.originator.getStateFromMemento(memento)

editor = Editor()
editor.typeStr("hello, ")
editor.typeStr("John")
print editor
editor.undo()
editor.typeStr("Mike")
print editor
editor.replaceStr("Fuck you, Mike")
print editor
editor.undo()
print editor
editor.undo()
print editor
