from .Config.api import query, commit
from decimal import Decimal


def getData(table):
	cmd = r'select * from %s' % table
	print(cmd)
	res = query(cmd)
	query(r'delete from %s' % table)
	return res


tableName = ''


def setTableName(table):
	global tableName
	tableName = table


def getDataFromClear(field):
	return query(r'select `%s` from %s' % (field, tableName))[0][0]


def updateData(field, value):
	print(field, value)
	query(r'update %s set `%s` = %s' % (tableName, field, value))


def clear_chang_video_speed():
	res = getData('chang_video_speed')
	setTableName('clear_chang_video_speed')
	oldDuration = getDataFromClear('oldDuration')
	newDuration = getDataFromClear('newDuration')
	oldSize = getDataFromClear('oldSize')
	newSize = getDataFromClear('newSize')
	oldFPS = getDataFromClear('oldFPS')
	newFPS = getDataFromClear('newFPS')
	timeSet = set()
	for i in res:
		timeSet.update([i[:6]])
		oldDuration += i[8]
		newDuration += i[8] / Decimal(i[7])
		oldSize += i[9]
		newSize += i[10]
		oldFPS += i[11]
		newFPS += i[12]
	times = getDataFromClear('times') + len(timeSet)
	items = getDataFromClear('items') + len(res)
	updateData('times', times)
	updateData('items', items)
	updateData('oldDuration', oldDuration)
	updateData('newDuration', newDuration)
	updateData('oldSize', oldSize)
	updateData('newSize', newSize)
	updateData('oldFPS', oldFPS)
	updateData('newFPS', newFPS)


def clear_delStr():
	res = getData('del_str')
	setTableName('clear_del_str')
	oldCharacters = getDataFromClear('oldCharacters')
	newCharacters = getDataFromClear('newCharacters')
	timeSet = set()
	for i in res:
		timeSet.update([i[:6]])
		oldCharacters += len(i[7])
		newCharacters += len(i[8])
	times = getDataFromClear('times') + len(timeSet)
	items = getDataFromClear('items') + len(res)
	updateData('times', times)
	updateData('items', items)
	updateData('oldCharacters', oldCharacters)
	updateData('newCharacters', newCharacters)
