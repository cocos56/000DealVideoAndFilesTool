from .Config.api import query
from os.path import join


def getData(timestamp):
    cmd = r"""select * from del_str where `year`='%s' and
                    `month`='%s' and `day`='%s' and `hour`='%s'
                    and `minute`='%s' and `second`='%s'
                """ % (timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute,
                       timestamp.second)
    r = query(cmd)
    res = []
    for i in r:
        res.append(i[6:])
    print(len(res))
    return res


def getFromDelStr(timestamp):
    data = getData(timestamp)
    r = []
    for i in data:
        r.append([join(i[0], i[1]), join(i[0], i[2])])
    return r
