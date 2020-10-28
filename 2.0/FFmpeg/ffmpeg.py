import psutil
from os.path import exists, isfile, splitext, split
from os import system
from Video.api import Video
from datetime import datetime
from Config.api import workDirs
from psutil import cpu_count


def runFFmpeg(i, speed=1, fps=10, threads=cpu_count(), quiet=True):
    with open('video.txt', 'w+', encoding='utf-8') as f:
        f.write(i)
        f.close()
    return FFmpeg(i, speed, fps, threads, quiet).o


class FFmpeg:
    cnt = 1

    @classmethod
    def addCnt(cls):
        cls.cnt += 1

    def __init__(self, i, speed, fps, threads, quiet):
        suffix = '_coco56_speed=%s.mp4' % str(speed)
        if suffix in split(i)[1]:
            return
        if exists(i) and isfile(i):
            self.i = i
        else:
            raise ParameterError(i, '输入的路径不存在或者不是文件的路径')
        self.o = splitext(i)[0] + suffix
        self.video = Video(i)
        self.fps = fps if self.video.fps > fps else self.video.fps
        self.speed = speed
        self.threads = psutil.cpu_count(threads >= 1)
        self.quiet = quiet
        self.cmd = 'ffmpeg'
        self.initCmd()
        print(self.cnt, self.cmd)
        old = datetime.now()
        print('\t', '任务开始于', old)
        for workDir in workDirs:
            if workDir == self.i[:len(workDir)]:
                print('\t', self.i.replace(workDir + '\\', '', 1)
                      , '-->', self.o.replace(workDir + '\\', '', 1))
        system(self.cmd)
        now = datetime.now()
        print('\t', '任务结束于', now)
        print('\t', '历时', now - old)
        self.addCnt()

    def initCmd(self):
        # initQuiet
        if self.quiet:
            self.cmd += ' -loglevel quiet'
        # initThread
        self.cmd += ' -threads %d' % self.threads
        self.cmd += ' -i "%s" -max_muxing_queue_size 1024' % self.i
        # initFPS(self):
        # initSpeed(self):
        if self.speed == 1:
            pass
        elif self.video.hasAudio():
            self.cmd += ' -filter_complex "[0:v]setpts=%s*PTS[v];[0:a]atempo=%s[a]" -map "[v]" -map "[a]"' % \
                        (str(1 / self.speed), str(self.speed))
        else:
            self.cmd += ' -filter:v "setpts=%s*PTS"' % str(1 / self.speed)
        self.cmd += ' -threads %d -r %d -metadata comment=coco56 "%s" -n' % (self.threads, self.fps, self.o)


class ParameterError(Exception):

    def __init__(self, para, explain=''):
        self.para = para
        self.explain = explain

    def __str__(self):
        return "参数错误：%s\n\t%s" % (self.para, self.explain)
