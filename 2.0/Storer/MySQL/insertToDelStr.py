from .Config.api import query, commit, Timestamp
from pymysql import escape_string


def insertToDelStr(fatherDir, oldName, newName):
    cmd = r"""insert into del_str
        (`year`, `month`, `day`, `hour`, `minute`,
        `second`, `fatherDir`, `oldName`, `newName`)
        value('%s', '%s', '%s', '%s', '%s',
        '%s', '%s', '%s', '%s')
        """ % (Timestamp.year, Timestamp.month, Timestamp.day, Timestamp.hour, Timestamp.minute,
               Timestamp.second, escape_string(fatherDir), oldName, newName)
    print(cmd)
    query(cmd)
    commit()
