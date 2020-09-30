from os import remove, system
from os.path import splitext, exists, split
from Name.getName import getName
from .video import Video, GetVideo
from Storer.MySQL.mysql import insertToChangVideoSpeed
from Path.api import getFiles
from .error import DamagedVideosExistError



class ReplaceAudio:
    suffix = '_coco56_merge.mp4'

    def __init__(self):
        self.replaceAudio()
        self.deleteOldFiles()

    @classmethod
    def getOutput(cls, i):
        return splitext(i)[0] + cls.suffix

    def replaceAudio(self):
        print('正在对视频中的音频进行替换......')
        cnt = 0
        for i in getFiles(True):
            # print(i)
            o = self.getOutput(i)
            # print(getName(i))
            if not Video.isVideo(i):
                continue
            elif '_get_vedio' in getName(i):
                continue
            elif Video.isDamaged(i):
                raise DamagedVideosExistError(i)
            mp3 = splitext(i)[0] + '.mp3'
            if not exists(mp3):
                continue
            if exists(o):
                continue
            cnt += 1
            cmd = 'ffmpeg -loglevel quiet -i "%s" -i "%s" "%s"' % (splitext(i)[0] + GetVideo.suffix, mp3, o)
            print(cnt, cmd)
            system(cmd)
        print('音频替换完毕\n')

    def deleteOldFiles(self):
        cnt = 0
        for i in getFiles(False):
            if not Video.isVideo(i):
                continue
            elif self.suffix in split(i)[1]:
                continue
            elif '_get_vedio' in getName(i):
                continue
            cnt += 1
            print(cnt, i)
            mp3 = splitext(i)[0] + '.mp3'
            video = splitext(i)[0] + GetVideo.suffix
            m4a = splitext(i)[0] + '.m4a'
            insertToChangVideoSpeed(i, self.getOutput(i))
            remove(i)
            remove(mp3)
            remove(m4a)
            remove(video)
