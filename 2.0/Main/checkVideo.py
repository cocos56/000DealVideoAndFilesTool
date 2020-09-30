from Video.api import Video
from Path.api import removeFiles


if __name__ == '__main__':
    err = Video.getDamagedList()
    print(err)
    removeFiles(err)

