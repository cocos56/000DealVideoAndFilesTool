from os.path import splitext, basename


def getName(path): return splitext(basename(path))[0]