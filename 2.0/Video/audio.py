from Path.api import getFiles
from os.path import splitext, exists
from os import system
from .video import Video
from .error import DamagedVideosExistError


class GetAudio:
    suffix = '.m4a'

    def __init__(self):
        self.getAudio()

    @classmethod
    def getOutput(cls, i): return splitext(i)[0] + cls.suffix

    def getAudio(self):
        print('正在进行音频提取......')
        for i in getFiles(True):
            print(i)
            o = self.getOutput(i)
            if not Video.isVideo(i):
                continue
            elif Video.isDamaged(i):
                raise DamagedVideosExistError(i)
            elif exists(o):
                continue
            cmd = 'ffmpeg -loglevel quiet -i "%s" -vn -y -acodec copy "%s"' % (i, o)
            print(cmd)
            system(cmd)
        print('音频提取完毕\n')
