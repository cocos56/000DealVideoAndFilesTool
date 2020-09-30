import os
import datetime
import re


def findAllWithRe(data, pattern):
	expression = re.compile(pattern)
	res = expression.findall(data)
	return res


def addColonsToFilePath(s): return '"' + s + '"'


class FN:
	"""
	本类用于分析和更改当前目录下的所有文件名
	"""
	def __init__(self, workDir):
		self.workDir = workDir
		self.cwd = os.getcwd()
		self.filesName = []
		self.dirsName = []
		self.extensions = {}
		self.filesNum = {}
		self.log = []
		self.name = ''

	def analyzeExtensions(self, walkSub=True):
		self.__init__(self.workDir)

		self.__getFilesName(walkSub)
		for i in self.filesName:
			e = self.analyzeFN(i)[2]
			if e not in self.extensions:
				self.extensions.update({e: 1})
			else:
				self.extensions.update({e: self.extensions[e] + 1})
		self.__getFilesNum()

	def delFsStr(self, delS, reS='', exe=False):
		k = 1
		for i in self.filesName:
			print(i)
			t = self.__hasStr(i, delS)
			if (t[2]):
				new_name = t[1] + t[0].replace(delS, reS)
				if (exe and not i == new_name):
					os.rename(i, new_name)
					self.log.append(str(k) + ' ' + i + '-->' + new_name)
					print(k, i, '-->', new_name)
					k += 1
		self.name = '删除文件名中字符'
		self.__saveToLog()

	def delDsStr(self, delS, reS='', exe=False):
		k = 1
		for i in self.dirsName:
			print(i)
			t = self.__hasStr(i, delS)
			if (t[2]):
				new_name = t[1] + t[0].replace(delS, reS)
				if (exe and not i == new_name):
					os.rename(i, new_name)
					self.log.append(str(k) + ' ' + i + '-->' + new_name)
					print(k, i, '-->', new_name)
					k += 1
		self.name = '删除文件名中字符'
		self.__saveToLog()

	def delFsStrWithRe(self, pattern, exe=False):
		k = 1
		for i in self.filesName:
			fn = self.analyzeFN(i)
			res = findAllWithRe(fn[1], pattern)
			print(i)
			print("res=", res)
			if res:
				res = res[0]
				new_name = "".join(res)
				new_name = fn[0] + new_name + fn[2]
				if exe:
					if i == new_name:
						break
					os.rename(i, new_name)
					self.log.append(str(k) + ' ' + i + '-->' + new_name)
					print(k, i, '-->', new_name)
					k += 1
				else:
					print("new_name=", new_name)
		self.name = '使用正则表达式删除文件名中字符'
		self.__saveToLog()

	def addFStr(self, s, addS, extension):
		'''
		addS 是在文件名与后缀名之间要添加的字符
		extension 是文件后缀名
		'''
		t = self.analyzeFN(s)
		new_name = t[0] + t[1] + addS + extension
		return new_name

	def analyzeFN(self, s):
		'''
		传入文件名s，返回t，其中t[0] 文件路径, t[1] 文件名（不含后缀）, t[2] 文件后缀（含'.'）
		s = [
			'01_考研形势',
			'01_考研形势.mp4',
			'D:\\01_考研形势',
			'D:\\01_考研形势.mp4'
		]
		'''

		t = ['', '', '']  # t[0] 文件路径, t[1] 文件名（不含后缀）, t[2] 文件后缀（含'.'）
		length = len(s)

		if (length == 0):
			return t

		while (s[length - 1] != '\\'):
			if (s[length - 1] == '.'):
				break
			elif (length == 1):
				t[1] = s  # 传入的字符串为纯文件名
				return t
			length -= 1

		if (s[length - 1] == '.'):  # 传入的字符串含后缀名
			t[2] = s[length - 1:]
			s = s[:length - 1]
			length -= 1
		elif (s[length - 1] == '\\'):  # 传入的字符串不含后缀名
			t[1] = s[length:]
			t[0] = s[:length]
			return t

		if (len(s) == 0):
			return t
		while (s[length - 1] != '\\'):
			if (length == 1):
				t[1] = s
				return t
			length -= 1
		t[1] = s[length:]
		t[0] = s[:length]
		return t

	def remove_end_space(self, s):
		s = s.replace(chr(160), ' ')
		length = len(s)
		while (length and s[length - 1] == ' '):
			length -= 1
		return s[:length]

	def __hasStr(self, s, delS):
		length = len(s)
		while (s[length - 1] != '\\'):
			length -= 1
		t = []
		t1 = s[length:]
		t2 = s[:length]
		t3 = t1.find(delS) != -1
		t.append(t1)
		t.append(t2)
		t.append(t3)
		# print(t1)
		# print(t2)
		return t

	def __getFilesName(self, walkSub):
		print(self.workDir)
		for root, dirs, files in os.walk(self.workDir):
			# print(root)	# 当前目录路径
			# print(dirs)	# 当前路径下的所有子目录
			# print(files)   # 当前目录下的所有非目录子文件
			if (not walkSub):
				if (not root == self.workDir):
					break
			for i in files:
				temp = root + '\\' + i
				if (i != ''):
					self.filesName.append(temp)
			for i in dirs:
				temp = root + '\\' + i
				if (i != ''):
					self.dirsName.append(temp)

	def __getFilesNum(self):
		sum = 0
		for k in self.extensions:
			self.filesNum.update({str(k): self.extensions[k]})
			sum += self.extensions[k]
		self.filesNum.update({'sum=': sum})

	def __saveToLog(self):
		time = str(datetime.datetime.now())
		time = time.replace(':', '：')
		logs_dir = self.cwd + '\\logs'
		if not os.path.exists(logs_dir):
			os.mkdir(logs_dir)
		logf = logs_dir + '\\' + self.name + '_log_' + time + '.txt'
		f = open(logf, 'a+', encoding='utf-8')
		for i in self.log:
			f.write(i + '\n')
		f.close()
		self.log = []
		print(self.name + '的日志文件已保存在：' + logf)
