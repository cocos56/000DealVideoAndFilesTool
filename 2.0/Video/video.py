from os.path import splitext, getsize, exists
from os import remove, system
import cv2
from moviepy.editor import VideoFileClip
from Config.api import videoSuffixes
from Path.api import getFiles
from datetime import datetime
from .error import VideoDecodeError, FFmpegCanNotDealError, DamagedVideosExistError


class CheckVideo:
	def __init__(self):
		self.checkVideo()

	def checkVideo(self):
		print('正在检查视频是否有损坏......')
		err = Video.getDamagedList()
		if err:
			raise DamagedVideosExistError(err)
		print('检查完毕，视频无损坏\n')


def fixUnicodeDecodeError(videoPath):
	now = datetime.now()
	suffix = '.mp4'
	if splitext(videoPath)[1] == suffix:
		suffix = '.avi'
	newVideo = splitext(videoPath)[0] + suffix
	cmd = 'ffmpeg -loglevel quiet -i "%s" "%s"' % (videoPath, newVideo)
	print(cmd)
	system(cmd)
	if exists(newVideo) and Video.isVideo(newVideo):
		remove(videoPath)
	else:
		raise FFmpegCanNotDealError(videoPath)
	print('处理UnicodeDecodeError历时：', datetime.now() - now)


class GetVideo:
	suffix = '_get_vedio.mp4'

	def __init__(self):
		self.getVideo()

	@classmethod
	def getOutput(cls, i):
		return splitext(i)[0] + cls.suffix

	def getVideo(self):
		print('正在进行纯视频（不含音频的视频）提取......')
		for i in getFiles(True):
			print(i)
			o = self.getOutput(i)
			if not Video.isVideo(i):
				continue
			elif Video.isDamaged(i):
				raise DamagedVideosExistError(i)
			elif exists(o):
				continue
			cmd = 'ffmpeg -loglevel quiet -i "%s" -vcodec copy -an "%s" -n' % (i, o)
			print(cmd)
			system(cmd)
		print('纯视频（不含音频的视频）提取完毕\n')


class Video:
	def __init__(self, videoPath):
		cap = cv2.VideoCapture(videoPath)
		try:
			clip = VideoFileClip(videoPath)
		except (UnicodeDecodeError, IOError) as e:
			cap.release()
			print(e)
			fixUnicodeDecodeError(videoPath)
			raise VideoDecodeError("'utf-8' codec can't decode : invalid start byte")
		self.audio = clip.audio
		self.duration = clip.duration  # 视频时长（s:秒）
		self.fps = clip.fps
		# self.fps = cap.get(cv2.CAP_PROP_FPS)
		# print(self.fps)
		self.width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		self.size = getsize(videoPath)
		cap.release()
		clip.close()

	def hasAudio(self):
		return self.audio is not None

	@classmethod
	def isDamaged(cls, videoPath):
		if not splitext(videoPath)[1].lower() in videoSuffixes:
			return False
		return not cls.isVideo(videoPath)

	@classmethod
	def isVideo(cls, file):
		if not splitext(file)[1].lower() in videoSuffixes:
			return False
		try:
			if cv2.VideoCapture(file).get(cv2.CAP_PROP_FPS) <= 0:
				fps = Video(file).fps
		# print(fps)
		except Exception as e:
			print(e)
			return False
		return True

	@classmethod
	def getDamagedList(cls):
		err = []
		for i in getFiles():
			print(i)
			if not exists(i):
				return cls.getDamagedList()
			if cls.isDamaged(i):
				err.append(i)
				print(i)
		return err
