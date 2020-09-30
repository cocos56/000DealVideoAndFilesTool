from re import compile
from os.path import basename, dirname, join
from os import rename
from Path.api import getFiles, getDirs
from .getName import getName
from .name import setNewName
from Storer.api import insertToDelStr


def findAllWithRe(data, pattern):
	expression = compile(pattern)
	res = expression.findall(data)
	# print(res)
	return res


def delFsStrWithRe(pattern, exe=False):
	cnt = 1
	for i in getFiles():
		res = findAllWithRe(getName(i), pattern)
		if not res:
			continue
		# print(i)
		newName = "".join(res[0])
		setNewName(newName, i, cnt, exe)
		cnt += 1


def delFsStr(oldStr, newStr='', exe=False):
	cnt = 1
	for i in getFiles():
		# print(getName(i))
		if oldStr not in getName(i):
			continue
		newName = getName(i).replace(oldStr, newStr, 1)
		setNewName(newName, i, cnt, exe)
		cnt += 1


def stripFileName(chars='', exe=False):
	cnt = 1
	for i in getFiles():
		# print(getName(i))
		oldName = getName(i)
		if chars == '':
			newName = getName(i).strip()
		else:
			newName = getName(i).strip(chars)
		if oldName == newName:
			continue
		setNewName(newName, i, cnt, exe)
		cnt += 1


def delDsStr(oldStr, newStr='', exe=False):
	cnt = 1
	for i in getDirs():
		if oldStr not in basename(i):
			continue
		fatherDir = dirname(i)
		newPath = join(fatherDir, basename(i).replace(oldStr, newStr))
		print(cnt, i, '-->', newPath)
		cnt += 1
		insertToDelStr(fatherDir, basename(i), basename(newPath))
		if exe:
			try:
				rename(i, newPath)
			except FileNotFoundError:
				return 'FileNotFoundError'
