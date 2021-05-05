class Button(object):
	def render(self):
		raise NotImplementedError


class WindowsButton(Button):
	def render(self):
		print "render WindowsButton"


class HTMLButton(Button):
	def render(self):
		print "render HTMLButton"


class Dialog(object):
	def createButton(self):
		raise NotImplementedError

	def render(self):
		okButton = self.createButton()
		okButton.render()


class WindowsDialog(Dialog):
	def createButton(self):
		return WindowsButton()


class WebDialog(Dialog):
	def createButton(self):
		return HTMLButton()


class App(object):
	def __init__(self, os):
		if os == "Windows":
			self.dialog = WindowsDialog()
		else:
			self.dialog = WebDialog()

	def render(self):
		self.dialog.render()

app = App("Windows")
app.render()

app = App("Web")
app.render()
