from FN import FN
from CF import CF
import datetime
import os
import json
import subprocess
from time import sleep


class CV:
	'''
	本类用于处理视频
	'''

	def __init__(self, workDir, sleepTime=1):
		self.workDir = workDir
		self.FNIns = FN(self.workDir)
		self.FNIns.analyzeExtensions()
		self.log = []
		self.GSTime = datetime.datetime.now()
		self.vType = ['.mp4', '.avi', '.vob', '.mkv', '.VOB', '.flv', '.wmv', '.mov', '.rmvb', '.ts', '.mpg', '.webm']
		self.aType = ['.m4a']
		self.name = ''
		self.flag_start = True
		self.flag_stop = True
		self.cwd = os.getcwd()
		self.speed = 1
		self.dealOldFilesMode = 0
		self.sleepTime = sleepTime

	def sleep(self):
		print("休息：", self.sleepTime, "s")
		sleep(self.sleepTime)

	def DealVError(self, i, new_i):
		time = str(datetime.datetime.now())
		time = time.replace(':', '：')
		logs_dir = self.cwd + '\\logs'
		if not os.path.exists(logs_dir):
			os.mkdir(logs_dir)
		logf = logs_dir + '\\' + 'DealVedioError' + '_log_' + time + '.txt'
		with open(logf, 'w+', encoding='utf-8') as f:
			log = '检测到文件:\n' + i + '\n不是合法的视频文件（文件大小为0B或者是其他类型的文件），请尝试做删除或修复处理。'
			log += '\n若您确信是合法的视频文件（指用视频播放器可以正常播放的视频文件），请把此视频文件发送至我的邮箱zj175@139.com获取帮助。'
			f.write(log + '\n')
			f.close()
		print('DealVedioError' + '的日志文件已保存在：' + logf)
		logf_d = 'start \"\" \"' + logf + '\"'
		os.system(logf_d)
		dir = self.FNIns.analyzeFN(i)[0]
		os.system('start \"\" \"' + dir + '\"')
		s = input('请按回车键继续执行，若要退出请输入q然后回车\n')
		if s == '':
			if (os.path.exists(i)):
				os.rename(i, i + '.error')
				print('已将\n' + i + '\n更名为-->\n' + i + '.error\n')
			self.FNIns.analyzeExtensions()
			self.dealV(self.speed, self.dealOldFilesMode)
		else:
			os._exit(0)

	def dealV(self, speed=1, dealOldFilesMode=0, gpu=False, threads=1):
		self.__Start('视频倍速')
		self.speed = speed
		self.dealOldFilesMode = dealOldFilesMode
		aSpeed = speed
		vSpeed = 1 / speed
		c = 1
		s = '_coco56_speed=' + str(speed)
		cn = self.__getTasksNum(s)
		for i in self.FNIns.filesName:
			if (self.FNIns.analyzeFN(i)[2] in self.vType):
				LSTime = datetime.datetime.now()
				new_i = self.FNIns.addFStr(i, s, '.mp4')
				if (not os.path.exists(new_i) and i.find(s) == -1):
					i_d = i
					i = '\"' + i + '\"'
					new_i_d = new_i
					new_i = '\"' + new_i + '\"'
					print('正在执行：', c, '/', cn, ' ', i, '-->', new_i, ' 请稍后。。。', sep='')
					# if(gpu):
					# if(speed != 1):
					# cmd = 'ffmpeg -loglevel quiet -threads 8 -i ' + i + ' -threads 8 -filter_complex "[0:v]setpts=' + str(vSpeed) + '*PTS[v];[0:a]atempo=' + str(aSpeed) + '[a]" -map "[v]" -map "[a]" ' + new_i
					# else:
					#         cmd = 'ffmpeg -loglevel quiet -i ' + i + ' ' + new_i
					# else:
					if (speed != 1):
						cmd = 'ffmpeg -loglevel quiet -threads ' + str(threads) + ' -i ' + i + ' -threads ' + str(
							threads) + ' -filter_complex "[0:v]setpts=' + str(vSpeed) + '*PTS[v];[0:a]atempo=' + str(
							aSpeed) + '[a]" -map "[v]" -map "[a]" -r 15 ' + new_i
					else:
						cmd = 'ffmpeg -loglevel quiet -i ' + i + ' ' + new_i
					# print(cmd)
					os.system(cmd)
					LETime = datetime.datetime.now()
					text = '此子任务开始于：' + str(LSTime) + '    总历时：' + str(LETime - LSTime)
					print(text)
					status = '任务完成状态：'
					if os.path.exists(new_i_d):
						size = os.path.getsize(new_i_d)
						if (not size == 0):
							status += '成功'
						else:
							self.DealVError(i_d, new_i_d)
					else:
						self.DealVError(i_d, new_i_d)
					print(status)
					self.log.append(str(c) + '  ' + i + '-->' + new_i + '\n' + text + '\n' + status)
					c += 1
					self.sleep()
		d1 = CF(self.workDir)
		if (dealOldFilesMode == 0):
			d1.MoveOldFiles(self.vType, Str=s)
		elif (dealOldFilesMode == 1):
			d1.DelOldFiles(self.vType, Str=s)
		self.__Stop()

	def Transcode(self, aimedFormat='.mp4', dealOldFilesMode=0):
		self.__Start('视频转码')
		self.dealOldFilesMode = dealOldFilesMode
		c = 1
		s = '_coco56_transcode'
		cn = self.__getTasksNum(s)
		for i in self.c1.filesName:
			if (self.c1.analyzeFN(i)[2] in self.vType):
				LSTime = datetime.datetime.now()
				new_i = self.c1.addFStr(i, s, aimedFormat)
				if (not os.path.exists(new_i) and i.find(s) == -1):
					i_d = i
					i = '\"' + i + '\"'
					new_i_d = new_i
					new_i = '\"' + new_i + '\"'
					print('正在执行：', c, '/', cn, ' ', i, '-->', new_i, ' 请稍后。。。', sep='')
					cmd = 'ffmpeg -loglevel quiet -i ' + i + ' -vcodec copy -acodec copy -vbsf h264_mp4toannexb ' + new_i
					print(cmd)
					os.system(cmd)
					LETime = datetime.datetime.now()
					text = '此子任务开始于：' + str(LSTime) + '    总历时：' + str(LETime - LSTime)
					print(text)
					status = '任务完成状态：'
					if os.path.exists(new_i_d):
						size = os.path.getsize(new_i_d)
						if (not size == 0):
							status += '成功'
						else:
							self.DealVError(i_d, new_i_d)
					else:
						self.DealVError(i_d, new_i_d)
					print(status)
					self.log.append(str(c) + '  ' + i + '-->' + new_i + '\n' + text + '\n' + status)
					c += 1
		if (dealOldFilesMode == 0):
			pass
		elif (dealOldFilesMode == 1):
			d1 = CF.CF()
			d1.MoveOldFiles(self.vType, Str=s)
		self.__Stop()

	def V2A(self):
		self.__Start('视频转音频')
		c = 1
		for i in self.c1.filesName:
			if (self.c1.analyzeFN(i)[2] in self.vType):
				LSTime = datetime.datetime.now()
				new_i = self.c1.addFStr(i, '', '.mp3')
				i = '\"' + i + '\"'
				new_i = '\"' + new_i + '\"'
				print(c, i, '-->', new_i)
				cmd = 'ffmpeg -loglevel quiet -i ' + i + ' ' + new_i
				# print(cmd)
				os.system(cmd)
				LETime = datetime.datetime.now()
				self.log.append(str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
					LETime - LSTime))
				c += 1
		self.__Stop()

	def getA(self):
		self.__Start('提取音频')
		c = 1
		for i in self.FNIns.filesName:
			if (self.FNIns.analyzeFN(i)[2] in self.vType):
				LSTime = datetime.datetime.now()
				new_i = self.FNIns.addFStr(i, '', '.m4a')
				i = '\"' + i + '\"'
				new_i = '\"' + new_i + '\"'
				print(c, i, '-->', new_i)
				cmd = 'ffmpeg -loglevel quiet -i ' + i + ' -vn -y -acodec copy ' + new_i
				# print(cmd)
				os.system(cmd)
				LETime = datetime.datetime.now()
				self.log.append(str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
					LETime - LSTime))
				c += 1
		self.__Stop()

	def getV(self):
		self.__Start('提取视频')
		c = 1
		s = '_get_vedio'
		s2 = '_coco56_merge'
		for i in self.FNIns.filesName:
			if (self.FNIns.analyzeFN(i)[2] in self.vType):
				LSTime = datetime.datetime.now()
				new_i = self.FNIns.addFStr(i, s, '.mp4')
				if (not os.path.exists(new_i) and i.find(s) == -1 and i.find(s2) == -1):
					i = '\"' + i + '\"'
					new_i = '\"' + new_i + '\"'
					print(c, i, '-->', new_i)
					# ffmpeg -i test.mp4 -vcodec copy -an 视频流.avi
					cmd = 'ffmpeg -loglevel quiet -i ' + i + ' -vcodec copy -an ' + new_i
					# print(cmd)
					os.system(cmd)
					LETime = datetime.datetime.now()
					self.log.append(
						str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
							LETime - LSTime))
					c += 1
		self.__Stop()
		pass

	def dealA(self):
		self.__Start('音频转码')
		c = 1
		for i in self.FNIns.filesName:
			if (self.FNIns.analyzeFN(i)[2] in self.aType):
				LSTime = datetime.datetime.now()
				new_i = self.FNIns.addFStr(i, '', '.mp3')
				i = '\"' + i + '\"'
				new_i = '\"' + new_i + '\"'
				print(c, i, '-->', new_i)
				# ffmpeg -i test.wav -f mp3 -acodec libmp3lame -y wav2mp3.mp3
				cmd = 'ffmpeg -i ' + i + ' -f mp3 -acodec libmp3lame -y ' + new_i
				print(cmd)
				os.system(cmd)
				LETime = datetime.datetime.now()
				self.log.append(str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
					LETime - LSTime))
				c += 1
		self.__Stop()

	def ReplaceAudio(self, dealOldFilesMode=0):
		self.getV()
		self.__Start('合并音频和视频')
		c = 1
		s = '_coco56_merge'
		cn = self.__getTasksNum(s)
		for i in self.FNIns.filesName:
			if (self.FNIns.analyzeFN(i)[2] == '.mp3'):
				LSTime = datetime.datetime.now()
				new_i = self.FNIns.addFStr(i, '_coco56_merge', '.mp4')
				if (not os.path.exists(new_i) and i.find(s) == -1):
					i_v = self.FNIns.addFStr(i, '_get_vedio', '.mp4')
					i_v = '\"' + i_v + '\"'
					i_a = '\"' + i + '\"'
					new_i = '\"' + new_i + '\"'
					print(c, '/', cn, ' ', i_a, ' and ', i_v, '-->', new_i, sep='')
					# ffmpeg -i 视频流.avi -i 音频流.mp3 -vcodec mpeg4 -acodec copy 合并.mp4
					cmd = 'ffmpeg -loglevel quiet -i ' + i_v + ' -i ' + i_a + ' ' + new_i
					# print(cmd)
					os.system(cmd)
					LETime = datetime.datetime.now()
					self.log.append(
						str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
							LETime - LSTime))
					c += 1
					self.sleep()
		if (dealOldFilesMode == 0):
			pass
		elif (dealOldFilesMode == 1):
			d1 = CF(self.workDir)
			Type = self.vType
			Type.append('.m4a')
			Type.append('.mp3')
			d1.MoveOldFiles(Type, Str='_coco56_merge')
		self.__Stop()

	def cTs(self, transTsToMp4=False, DelOldFiles=False):
		self.__Start('处理ts文件')
		text = '\n补齐ts文件名：把文件名通过前补零的方式都补足6位'
		self.log.append(text)
		print(text)
		self.__fillTsName()

		text = '\n合并ts文件'
		self.log.append(text)
		print(text)
		self.combineTs()

		if (transTsToMp4):
			text = '\n转换ts文件为mp4文件'
			self.log.append(text)
			print(text)
			self.__tTs()
		if (DelOldFiles):
			text = '\n删除旧ts文件'
			self.log.append(text)
			print(text)
			self.__delOldTs()
		self.__Stop()

	def dHls(self, DelOldFiles=False):
		self.__Start('处理使用HLS协议的m3u8文件')
		c = 1
		cwd = self.cwd
		D = cwd + '\InputFiles'
		oD = cwd + '\OutputFiles'
		os.chdir(D)
		if (not os.path.exists(oD)):
			os.mkdir(oD)
		self.c1.analyzeExtensions(walkSub=False, walkDir=D)
		# print(self.c1.filesName)
		for i in self.c1.filesName:
			analyze = self.c1.analyzeFN(i)
			analyze[1] = self.c1.remove_end_space(analyze[1])
			i2 = analyze[0] + analyze[1] + analyze[2]
			if not i == i2:
				os.rename(i, i2)
				i = i2
			new_i = analyze[0] + analyze[1] + '_coco56' + analyze[2]
			if (analyze[2] == '.m3u8' and analyze[1].find('_coco56') == -1 and not os.path.exists(new_i)):
				LSTime = datetime.datetime.now()
				print(c, i, '-->', new_i)
				self.modifyM3u8(i, new_i, D, analyze[1])
				LETime = datetime.datetime.now()
				c += 1
				mp4_i = oD + '\\' + analyze[1] + '_coco56' + '.mp4'
				cmd = 'ffmpeg -i "' + new_i + '" -c copy -bsf:a aac_adtstoasc "' + mp4_i + '"'
				p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				self.log.append(str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
					LETime - LSTime))
				# break
		os.chdir(self.cwd)
		self.__Stop()

	def modifyM3u8(self, old, new, Dir, fn):
		data = []
		with open(old, 'r', encoding='utf-8') as f:
			lines = f.readlines()
			for line in lines:
				line = line.replace('file:///storage/emulated/0/QQBrowser/视频/', '')
				bI = line.find('URI=')
				if (not bI == -1):
					eI = line.find(',IV=')
					kF = line[bI + 5:eI - 1]
					# s = self.chDirN(kF, Dir, fn)
					new_kF = kF.replace('.key', '.m3u8')
					if (os.path.exists(Dir + '\\' + kF)):
						os.rename(Dir + '\\' + kF, Dir + '\\' + new_kF)
					# new_kF = new_kF.replace(s, fn)
					# print(kF, new_kF)
					line = line.replace(kF, new_kF)
				data.append(line)
				# print(line,end='')
			f.close()
		with open(new, 'w', encoding='utf-8') as f:
			f.writelines(data)
			f.close()

	def chDirN(self, s, cwd, fn):
		l = len(s) - 1
		while (l):
			if (s[l] == '/'):
				break
			l -= 1
		s = s[:l]
		if (os.path.exists(cwd + '\\' + s)):
			os.rename(s, fn)
		return s

	def cutV(self, cutBegin, cutEnd, dealOldFilesMode=0):
		self.__Start('剪切视频文件')
		c = 1
		cn = self.__getTasksNum(s='_cococ56_cut')
		for i in self.FNIns.filesName:
			if self.FNIns.analyzeFN(i)[2] in self.vType:
				beginTime = datetime.timedelta(seconds=cutBegin)
				endTime = datetime.timedelta(seconds=float(self.__getVSeconds(i)) - cutEnd)
				LSTime = datetime.datetime.now()
				new_i = self.FNIns.addFStr(i, '_cococ56_cut', '.mp4')
				if not os.path.exists(new_i) and i.find('_cococ56_cut') == -1:
					i = '\"' + i + '\"'
					new_i = '\"' + new_i + '\"'
					# ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy -copyts cut.mp4
					print(c, '/', cn, ' ', i, '-->', new_i, sep='')
					cmd = 'ffmpeg' + ' -i ' + i + ' -ss ' + str(beginTime) + r' -to ' + str(
						endTime) + r' -c copy ' + new_i
					print(cmd)
					os.system(cmd)
					LETime = datetime.datetime.now()
					self.log.append(
						str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
							LETime - LSTime))
					c += 1
		d1 = CF(self.workDir)
		if dealOldFilesMode == 0:
			d1.MoveOldFiles(self.vType, Str='_cococ56_cut')
		elif dealOldFilesMode == 1:
			d1.DelOldFiles(self.vType, Str='_cococ56_cut')
		self.__Stop()

	def split_OneVedio_Into_MultipleVedios_WithNumber(self, number=1, dealOldFilesMode=0):
		'''
		用于将一个视频分割成多个视频，默认情况下分割成的文件数为1（即number值为1）
		dealOldFilesMode为0代表处理完后不删除也不移动源文件（默认）
		dealOldFilesMode为1代表处理完后移动所有源文件到当前工作目录下的一个新的以当前时间（精确到毫秒）命名的文件夹

		此方法以传入的数字为分隔依据，还打算开发以时间为分隔依据以及以大小为分隔依据。
		以数字为分隔依据就是说把一个视频分割成多少个，每一个视频的时长都等于原视频时长的n分之一（n为传入的参数number）。
		以时间为分隔依据就是说把一个视频分割成每个视频片段的时长都等于传入的时间（最后一个视频片段除外，因为在相除之后可能存在余数）
		以大小为分隔依据就是说把一个视频分割成每个视频片段的大小都等于传入的大小（同样最后一个视频片段除外，因为在相除之后可能存在余数）
		'''
		self.__Start('分割视频文件')
		s = '_cococ56_split'
		c = 1
		cn = self.__getTasksNum(s)
		for i in self.c1.filesName:
			if (self.c1.analyzeFN(i)[2] in self.vType):
				totalTime = float(self.__getVSeconds(i))
				splitTime = totalTime / number
				endTimeList = [x * splitTime for x in range(1, number)]
				endTimeList.append(totalTime)
				beginTime = 0
				partNum = 1
				for endTime in endTimeList:
					LSTime = datetime.datetime.now()
					new_i = self.c1.addFStr(i, s + '_part_' + str(partNum), '.mp4')
					if (not os.path.exists(new_i) and i.find(s) == -1):
						i = '\"' + i + '\"'
						new_i = '\"' + new_i + '\"'
						print(c, '/', cn, ' ', partNum, '/', number, ' ', i, '-->', new_i, sep='')
						# ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy -copyts cut.mp4
						cmd = 'ffmpeg' + ' -i ' + i + ' -ss ' + str(beginTime) + r' -to ' + str(
							endTime) + r' -c copy ' + new_i
						print(cmd)
						os.system(cmd)
						LETime = datetime.datetime.now()
						self.log.append(
							str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
								LETime - LSTime))
						partNum += 1
						beginTime = endTime
				c += 1
		if (dealOldFilesMode == 0):
			pass
		elif (dealOldFilesMode == 1):
			d1 = CF.CF()
			Str = '_cococ56_cut'
			d1.MoveOldFiles(self.vType, Str=Str)
		self.__Stop()

	def __getVSeconds(self, filename):
		command = ["ffprobe.exe", "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
				   filename]
		result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		out = result.stdout.read()
		# print(str(out))
		temp = str(out.decode('utf-8'))
		seconds = json.loads(temp)["format"]['duration']
		return seconds

	def __getTasksNum(self, s):
		num = 0
		for i in self.FNIns.filesName:
			if (self.FNIns.analyzeFN(i)[2] in self.vType):
				new_i = self.FNIns.addFStr(i, s, '.mp4')
				if (not os.path.exists(new_i) and i.find(s) == -1):
					num += 1
		return num

	def __delOldTs(self):
		c = 1
		for i in self.c1.filesName:
			analyze = self.c1.analyzeFN(i)
			if (analyze[2] == '.ts' and not analyze[1] == '0000000new'):
				text = str(c) + '  已删除：' + i
				os.remove(i)
				print(text)
				self.log.append(text)
				c += 1

	def __tTs(self):
		cwd = os.getcwd()
		father_dir = cwd
		i = '0000000new.ts'
		new_i = '0000000new.mp4'
		new_file = father_dir + '\\' + new_i
		if (not os.path.exists(new_file)):
			cmd = 'ffmpeg -i ' + i + ' ' + new_i
			self.log.append(cmd)
			os.chdir(father_dir)
			os.system(cmd)
			os.chdir(cwd)

	def combineTs(self):
		cwd = os.getcwd()
		aim_dir = cwd
		new_ts = '0000000new.ts'
		new_ts_file = aim_dir + '\\' + new_ts
		if not os.path.exists(new_ts_file):
			cmd = 'ffmpeg -i "concat:'
			c = 1
			for i in self.c1.filesName:
				analyze = self.c1.analyzeFN(i)
				if (analyze[2] == '.ts'):
					if not c == 1:
						cmd += '|'
					temp = analyze[1] + analyze[2]
					print(temp)
					cmd += temp
					c += 1
			cmd += '" -acodec copy -vcodec copy -absf aac_adtstoasc '
			cmd += new_ts
			self.log.append(cmd)
			os.chdir(aim_dir)
			print(cmd)
			print(os.getcwd())
			os.system(cmd)
			os.chdir(cwd)

	def __fillTsName(self):
		c = 1
		for i in self.c1.filesName:
			analyze = self.c1.analyzeFN(i)
			if (analyze[2] == '.ts'):
				LSTime = datetime.datetime.now()
				new_i = analyze[0] + analyze[1].zfill(6) + analyze[2]
				if not i == new_i:
					print(c, i, '-->', new_i)
					os.rename(i, new_i)
					LETime = datetime.datetime.now()
					c += 1
					self.log.append(
						str(c) + '  ' + i + '-->' + new_i + '\n' + '此子任务开始于：' + str(LSTime) + '    总历时：' + str(
							LETime - LSTime))
		self.c1.analyzeExtensions()

	def __Start(self, name):
		self.name = name
		self.log.append(self.name + '任务开始于：' + str(self.GSTime))

	def __Stop(self):
		print(self.FNIns.filesNum)
		self.GETime = datetime.datetime.now()
		print(self.GETime - self.GSTime)
		self.log.append(self.name + '任务结束于' + str(self.GETime) + '    总历时:' + str(self.GETime - self.GSTime))

		time = str(datetime.datetime.now())
		time = time.replace(':', '：')
		logs_dir = self.cwd + '\\logs'
		if not os.path.exists(logs_dir):
			os.mkdir(logs_dir)
		logf = logs_dir + '\\' + self.name + '_log_' + time + '.txt'
		with open(logf, 'w+', encoding='utf-8') as f:
			for i in self.log:
				f.write(i + '\n')
			f.close()
		self.log = []
		print(self.name + '的日志文件已保存在：' + logf)