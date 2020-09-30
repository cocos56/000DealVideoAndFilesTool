class VideoDecodeError(Exception):

	def __init__(self, text): self.text = text

	def __str__(self): return self.text


class FFmpegCanNotDealError(Exception):
	def __init__(self, text): self.text = text

	def __str__(self): return self.text


class DamagedVideosExistError(Exception):

	def __init__(self, videos): self.videos = videos

	def __str__(self): return '视频出现损坏，损坏的视频如下：\n' + str(self.videos)
