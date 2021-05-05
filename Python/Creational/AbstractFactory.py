class Button(object):
	def render(self):
		raise NotImplementedError


class WindowsButton(Button):
	def render(self):
		print "render WindowsButton"


class MacButton(Button):
	def render(self):
		print "render MacButton"


class Checkbox(object):
	def render(self):
		raise NotImplementedError


class WindowsCheckbox(Checkbox):
	def render(self):
		print "render WindowsCheckbox"


class MacCheckbox(Checkbox):
	def render(self):
		print "render MacCheckbox"


class GUIFactory(object):
	def createButton(self):
		raise NotImplementedError

	def createCheckbox(self):
		raise NotImplementedError


class WindowsFactory(GUIFactory):
	def createButton(self):
		return WindowsButton()

	def createCheckbox(self):
		return WindowsCheckbox()


class MacFactory(GUIFactory):
	def createButton(self):
		return MacButton()

	def createCheckbox(self):
		return MacCheckbox()


class App(object):
	def __init__(self, factory):
		self.factory = factory
		self.button = self.checkbox = None

	def createUI(self):
		self.button = self.factory.createButton()
		self.checkbox = self.factory.createCheckbox()

	def render(self):
		self.button and self.button.render()
		self.checkbox and self.checkbox.render()


class AppConfig(object):
	def main(self):
		global config
		if config == "Windows":
			factory = WindowsFactory()
		else:
			factory = MacFactory()

		self.app = App(factory)
		self.app.createUI()
		self.app.render()

config = "Windows"
AppConfig().main()
print "++++++++++++++++++++++++++++++++++++++++"
config = "Mac"
AppConfig().main()

