from functools import partial

class Command(object):
    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = ""

    def saveBackup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    def execute(self):
        raise NotImplementedError


class CopyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.getSelection()
        return False


class CutCommand(Command):
    def execute(self):
        self.saveBackup()
        self.app.clipboard = self.editor.getSelection()
        self.editor.deleteSelection()
        return True


class PasteCommand(Command):
    def execute(self):
        self.saveBackup()
        self.editor.replaceSelection(self.app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False


class CommandHistory(object):
    def __init__(self):
        self.history = []

    def push(self, c):
        self.history.append(c)

    def pop(self):
        if not self.history:
            return
        res = self.history[-1]
        self.history = self.history[:-1]
        return res


class Editor(object):
    def __init__(self):
        self.text = ""

    def getSelection(self):
        return self.text

    def deleteSelection(self):
        self.text = ""

    def replaceSelection(self, t):
        self.text = t


class Button(object):
    def __init__(self):
        self.command = None

    def setCommand(self, command):
        self.command = command

    def onClick(self):
        self.command and self.command()


class KeyboardListener(object):
    def __init__(self):
        self.hotkey_map = {}

    def add_listener(self, key, func):
        self.hotkey_map[key] = func

    def on_listen(self, key):
        if key not in self.hotkey_map:
            return
        self.hotkey_map[key]()


class Application(object):
    def __init__(self):
        self.clipboard = ""
        self.editor = Editor()
        self.history = CommandHistory()
        self.keyboard = KeyboardListener()

        def copy_func():
            self.executeCommand(CopyCommand(self, self.editor))

        def cut_func():
            self.executeCommand(CutCommand(self, self.editor))

        def paste_func():
            self.executeCommand(PasteCommand(self, self.editor))

        def undo_func():
            self.executeCommand(UndoCommand(self, self.editor))

        self.cut_button = Button()
        self.cut_button.setCommand(cut_func)
        self.copy_button = Button()
        self.copy_button.setCommand(copy_func)
        self.paste_button = Button()
        self.paste_button.setCommand(paste_func)
        self.undo_button = Button()
        self.undo_button.setCommand(undo_func)

        self.keyboard.add_listener("c+c", copy_func)
        self.keyboard.add_listener("c+x", cut_func)
        self.keyboard.add_listener("c+z", undo_func)
        self.keyboard.add_listener("c+v", paste_func)

    def executeCommand(self, command):
        if (command.execute()):
            self.history.push(command)

    def undo(self):
        command = self.history.pop()
        command and command.undo()


app = Application()
app.editor.text = "Hello Text"
app.cut_button.onClick()
print "text after cut: %s" % app.editor.text
app.keyboard.on_listen('c+v')
print "text after paste: %s" % app.editor.text

app.keyboard.on_listen('c+z')
app.undo_button.onClick()
print "text after cut and undo: %s" % app.editor.text

app.keyboard.on_listen('c+c')
app.editor.text = "fuck you"
app.paste_button.onClick()
print "text after copy, del and paste: %s" % app.editor.text
