from pymysql import connect
from pymysql.err import OperationalError
from datetime import datetime
from .hostConfig import host, port, database, user, password, charset
from os import system
from time import sleep


def backUp():
    cmd = r'mysqldump -h %s -P %s -u %s -p %s %s > F:\GP\000DealVideoAndFilesTool\2.0\Storer\MySQL\%s.sql' % (
        host, port, user, password, database, database)
    print(cmd)
    system(cmd)


class Timestamp:
    _dt = datetime.now()

    year = str(_dt.year)[-2:].rjust(2, '0')
    month = str(_dt.month).rjust(2, '0')
    day = str(_dt.day).rjust(2, '0')
    hour = str(_dt.hour).rjust(2, '0')
    minute = str(_dt.minute).rjust(2, '0')
    second = str(_dt.second).rjust(2, '0')


class Init:
    conn = None
    cs = None

    @classmethod
    def init(cls):
        # 创建Connection连接并获得Cursor对象
        try:
            cls.conn = connect(
                host=host, port=port, database=database,
                user=user, password=password, charset=charset)
            cls.cs = cls.conn.cursor()
        except OperationalError as e:
            print('init', e)
            sleep(30)
            cls.init()


Init.init()


def query(cmd):
    try:
        Init.cs.execute(cmd)
        results = Init.cs.fetchall()
    except OperationalError as e:
        print('query', e)
        sleep(30)
        Init.init()
        return query(cmd)
    return results


def commit():
    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    try:
        Init.conn.commit()
    except OperationalError as e:
        print('commit', e)
        sleep(30)
        Init.init()
        commit()
