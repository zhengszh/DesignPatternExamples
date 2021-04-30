class ComponentHelp(object):
    def showHelp(self):
        raise NotImplementedError

class Component(ComponentHelp):
    def __init__(self, help):
        self.help = help
        self.container = None

    def showHelp(self):
        if self.help:
            print "showHelp:%s" % self.help
        else:
            self.container.showHelp()

class Container(Component):
    def __init__(self, help):
        super(Container, self).__init__(help)
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.container = self

    def accept(self, v):
        v.visitCircle(self)

class Button(Container):
    pass

class Panel(Container):
    def __init__(self, help):
        super(Panel, self).__init__(help)
        self.model_text = ""

    def showHelp(self):
        if self.model_text:
            print "Show modal text:%s" % self.model_text
        else:
            super(Panel, self).showHelp()


class Dialog(Container):
    def __init__(self, help):
        super(Dialog, self).__init__(help)
        self.url = ""

    def showHelp(self):
        if self.url:
            print "Show url text:%s" % self.url
        else:
            super(Dialog, self).showHelp()


dialog = Dialog("Budget Reports")
dialog.url = "http://"
panel = Panel("")
panel.model_text = "This panel fucks"
ok = Button("")
ok.help = "ok button"
cancel = Button("")
panel.add(ok)
panel.add(cancel)
dialog.add(panel)

dialog.showHelp()
panel.showHelp()
ok.showHelp()
cancel.showHelp()
