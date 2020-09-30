from Path.api import getFilesType
from Video.api import ReplaceAudio
from Storer.api import commit
from datetime import datetime
from Video.api import GetVideo

now = datetime.now()

getFilesType()
GetVideo()
ReplaceAudio()
getFilesType()

print('总历时：', datetime.now()-now)
commit()
