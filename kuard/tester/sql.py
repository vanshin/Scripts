
from config import DATABASE
from qfcommon3.base import dbpool

from qfcommon3.base.dbpool import get_connection_exception, install


install(DATABASE)

def exp2sql(self, key, op, value):
    if '_' in value:
        value = value.replace('_', '\_')
    return dbpool.MySQLConnection.exp2sql(self, key, op, value)


dbpool.PyMySQLConnection.exp2sql = exp2sql


def main():
    with get_connection_exception('qf_core') as db:

        v = '%ktest_%'

        rt = db.select(
            table = 'profile',
            fields = 'name',
            where = {'name': ('like', v)},
        )
        print(rt)
        # ret = db.query("select name from where name like 'ktest|_%' escape '|'")
        # print(ret)

if __name__ == '__main__':
    main()

