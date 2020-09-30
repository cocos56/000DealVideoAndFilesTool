from Video.api import optimizeVideo

while True:
    res = optimizeVideo()
    if res == 'VideoDecodeError':
        pass
    else:
        break
# OptimizeVideo.removeComment()
