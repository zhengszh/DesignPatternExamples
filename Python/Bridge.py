class RemoteControl(object):
    def __init__(self, device):
        self.device = device

    def togglePower(self):
        if self.device.isEnabled():
            self.device.disable()
        else:
            self.device.enable()

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 10)

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 10)


class AdvanceRemoteControl(RemoteControl):
    def mute():
        self.device.setVolume(0)

class Devive(object):
    def isEnabled(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def getVolume(self):
        raise NotImplementedError

    def setVolume(self, v):
        raise NotImplementedError


class TV(Devive):
    def __init__(self):
        self.volume = 50
        self.enabled = False

    def isEnabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def getVolume(self):
        return self.volume

    def setVolume(self, v):
        self.volume = v


class Radio(Devive):
    def isEnabled(self):
        return True

    def enable(self):
        pass

    def disable(self):
        pass

    def getVolume(self):
        return 50

    def setVolume(self, v):
        pass

tv = TV()
print tv
remote = RemoteControl(tv)
remote.togglePower()
print tv.isEnabled()
print tv.getVolume()
remote.volumeUp()
print tv.getVolume()
remote.volumeDown()
print tv.getVolume()
remote.togglePower()
print tv.isEnabled()

radio = Radio()
remote = AdvanceRemoteControl(radio)
remote.togglePower()
print radio.isEnabled()
remote.volumeUp()
print radio.getVolume()
remote.volumeDown()
print radio.getVolume()
remote.togglePower()
print radio.isEnabled()
