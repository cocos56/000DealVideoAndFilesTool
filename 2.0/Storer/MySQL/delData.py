from .Config.api import query


def delData(timestamp):
    cmd = r"""delete from del_str where `year`='%s' and
                    `month`='%s' and `day`='%s' and `hour`='%s'
                    and `minute`='%s' and `second`='%s'
                """ % (timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute,
                       timestamp.second)
    query(cmd)
