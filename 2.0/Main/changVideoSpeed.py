from Video.api import changeVideoSpeed
from datetime import datetime
from Storer.api import commit

now = datetime.now()

speed = 1
speed = 1.1
speed = 1.2
# speed = 1.25
# speed = 1.28
# speed = 1.6
# speed = 2


while True:
	res = changeVideoSpeed(speed)
	if res == 'VideoDecodeError':
		pass
	else:
		break

print('总历时：', datetime.now()-now)
commit()
