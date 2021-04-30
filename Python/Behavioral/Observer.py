class EventManager(object):
    def __init__(self):
        self.listener_map = {}

    def subscribe(self, event_type, listener):
        self.listener_map.setdefault(event_type, [])
        l = self.listener_map[event_type]
        if listener not in l:
            l.append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type not in self.listener_map:
            return
        l = self.listener_map[event_type]
        if listener in l:
            l.remove(listener)
        if not l:
            self.listener_map.pop(event_type, None)

    def notify(self, event_type, data):
        for listener in self.listener_map.get(event_type, ()):
            listener.update(data)


class Editor(object):
    def __init__(self):
        self.file = ""
        self.event_manager = EventManager()

    def openFile(self, path):
        self.file = path
        print "open file:%s" % path
        self.event_manager.notify("open", path)

    def saveFile(self):
        print "save file: %s" % self.file
        self.event_manager.notify("save", self.file)


class EventListener(object):
    def update(self, data):
        raise NotImplementedError

class LogListener(EventListener):
    def update(self, data):
        print "[File Log] %s" % data

class EmailListener(EventListener):
    def update(self, data):
        print "Send Email to aa@aa.com: %s" % data

editor = Editor()
logger = LogListener()
email = EmailListener()
editor.event_manager.subscribe("open", logger)
editor.event_manager.subscribe("save", email)

editor.openFile("test.txt")
editor.saveFile()
print "++++++++++++++++++++"
editor.event_manager.unsubscribe("save", email)
editor.event_manager.subscribe("open", email)
editor.openFile("test.txt")
editor.saveFile()
