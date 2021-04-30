class VideoFile(object):
    def __init__(self, filename):
        pass

class OggCompressionCodec(object):
    pass

class MPEG4CompressionCodec(object):
    pass

class CodecFactory(object):
    @classmethod
    def extract(self, file):
        pass

class BitrateReader(object):
    @classmethod
    def read(self, filename, sourceCodec):
        pass

    @classmethod
    def convert(self, buffer, destinationCodec):
        pass

class AudioMixer(object):
    def fix(self, result):
        pass


class VideoConverter(object):
    def convert(self, filename, format):
        file = VideoFile(filename)
        sourceCodec = CodecFactory.extract(file)
        if format == "mp4":
            destinationCodec = MPEG4CompressionCodec()
        else:
            destinationCodec = OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (AudioMixer()).fix(result)
        return result

convertor = VideoConverter()
mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
print mp4
