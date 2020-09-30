from FFmpeg.api import runFFmpeg
from Path.api import getFiles
from .video import Video, CheckVideo
from .error import VideoDecodeError, DamagedVideosExistError
from os.path import splitext, split, exists
from os import remove
from Storer.api import insertToChangVideoSpeed
from psutil import cpu_count


def changeVideoSpeed(speed):
	try:
		ChangVideoSpeed(speed)
	except VideoDecodeError:
		return 'VideoDecodeError'


class ChangVideoSpeed:
	speed = 1
	fps = 10
	threads = cpu_count()
	suffix = '_coco56_speed=%s.mp4' % str(speed)

	@classmethod
	def setSpeed(cls, speed):
		cls.speed = speed
		cls.suffix = '_coco56_speed=%s.mp4' % str(speed)

	def __init__(self, speed=1):
		self.setSpeed(speed)
		CheckVideo()
		self.changeVideoSpeed()
		CheckVideo()
		self.deleteOldFiles()

	def changeVideoSpeed(self):
		print('正在进行视频倍速......')
		for i in getFiles(True):
			print(i)
			o = self.getOutput(i)
			if not Video.isVideo(i):
				continue
			elif Video.isDamaged(i):
				raise DamagedVideosExistError(i)
			elif exists(o):
				if Video.isDamaged(o):
					raise DamagedVideosExistError(i)
				continue
			runFFmpeg(i, self.speed, self.fps, self.threads)
		print('视频倍速处理完毕\n')

	@classmethod
	def getOutput(cls, i): return splitext(i)[0] + cls.suffix

	def deleteOldFiles(self):
		for i in getFiles(False):
			if not Video.isVideo(i):
				continue
			if self.suffix in split(i)[1]:
				continue
			insertToChangVideoSpeed(i, self.getOutput(i), self.speed)
			remove(i)
