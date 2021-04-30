class AudioPlayer(object):
    def __init__(self):
        self.state = ReadyState(self)
        self.playing = False

    def changeState(self, state):
        self.state = state

    def clickLock(self):
        self.state.clickLock()

    def clickPlay(self):
        self.state.clickPlay()

    def clickNext(self):
        self.state.clickNext()

    def clickPrevious(self):
        self.state.clickPrevious()

    def startPlayback(self):
        print "startPlayback"
        self.playing = True

    def stopPlayback(self):
        print "stopPlayback"
        self.playing = False

    def nextSong(self):
        print "nextSong"

    def previousSong(self):
        print "previousSong"


class State(object):
    def __init__(self, player):
        self.player = player

    def clickLock(self):
        raise NotImplementedError

    def clickPlay(self):
        raise NotImplementedError

    def clickNext(self):
        raise NotImplementedError

    def clickPrevious(self):
        raise NotImplementedError


class LockedState(State):

    def clickLock(self):
        if player.playing:
            self.player.changeState(PlayingState(self.player))
        else:
            self.player.changeState(ReadyState(self.player))

    def clickPlay(self):
        pass

    def clickNext(self):
        pass

    def clickPrevious(self):
        pass


class ReadyState(State):
    def clickLock(self):
        self.player.changeState(LockedState(self.player))

    def clickPlay(self):
        self.player.startPlayback()
        self.player.changeState(PlayingState(self.player))

    def clickNext(self):
        self.player.nextSong()

    def clickPrevious(self):
        self.player.previousSong()


class PlayingState(State):
    def clickLock(self):
        self.player.changeState(LockedState(self.player))

    def clickPlay(self):
        self.player.stopPlayback()
        self.player.changeState(ReadyState(self.player))

    def clickNext(self):
        self.player.nextSong()

    def clickPrevious(self):
        self.player.previousSong()


player = AudioPlayer()

player.clickPlay()
player.clickLock()
player.clickNext()
player.clickPrevious()
print "++++++++++++++++++++++++++++"
player.clickLock()
player.clickNext()
player.clickPrevious()
print "++++++++++++++++++++++++++++"
player.clickPlay()
player.clickPlay()
