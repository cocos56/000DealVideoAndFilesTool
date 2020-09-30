from pymediainfo import MediaInfo
from FFmpeg.api import runFFmpeg
from Path.api import getFiles
from os import remove, rename, system
from os.path import splitext, split, join
from time import sleep
from Storer.api import insertToChangVideoSpeed
from .video import Video
from .error import DamagedVideosExistError, VideoDecodeError


def isOptimized(videoPath):
    isContainedComment = MediaInfo.parse(videoPath).tracks[0].comment == 'coco56'
    isMp4 = splitext(videoPath)[1].lower() == '.mp4'
    return isContainedComment and isMp4


def isFlagRemoved(videoPath):
    return MediaInfo.parse(videoPath).tracks[0].comment is None


def optimizeVideo():
    try:
        OptimizeVideo()
    except VideoDecodeError:
        return 'VideoDecodeError'


class OptimizeVideo:
    def __init__(self):
        self.optimizeVideo()

    def optimizeVideo(self):
        print('正在进行视频优化......')
        for i in getFiles(True):
            print(i)
            if not Video.isVideo(i):
                continue
            elif isOptimized(i):
                continue
            elif Video.isDamaged(i):
                raise DamagedVideosExistError(i)
            o = runFFmpeg(i, threads=3)
            sleep(10)
            if Video.isDamaged(o):
                raise DamagedVideosExistError(i)
            insertToChangVideoSpeed(i, o)
            remove(i)
            rename(o, splitext(i)[0] + '.mp4')
        print('视频优化完毕\n')

    @classmethod
    def removeComment(cls):
        cnt = 0
        for i in getFiles(True):
            print(i)
            if not Video.isVideo(i):
                continue
            elif isFlagRemoved(i):
                continue
            elif Video.isDamaged(i):
                raise DamagedVideosExistError(i)
            o = join(split(i)[0], 'temp_coco56.mp4')
            cmd = r'ffmpeg -loglevel quiet -i "%s" -vcodec copy -acodec copy -metadata comment= "%s" -y' % (
                i, o)
            cnt += 1
            print(cnt, cmd)
            system(cmd)
            if Video.isDamaged(o):
                raise DamagedVideosExistError(o)
            insertToChangVideoSpeed(i, o)
            remove(i)
            rename(o, splitext(i)[0] + '.mp4')
        print('视频反优化完毕\n')
