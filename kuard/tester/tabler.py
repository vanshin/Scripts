
from qfcommon3.base.dbpool import get_connection

class Tabler(object):

    def __init__(self, db, table):
        self.db = db
        self.table = table


    @classmethod
    def from_info(cls, info):
        # FIXME 家电验证
        db, table = info.split('.')
        return cls(db, table)

    def query_one(self, where):
        with get_connection(self.db) as db:
            k = db.select_one(
                table = self.table,
                fields = '*',
                where=where
            ) or {}
        return k

    def del_one(self, where):
        with get_connection(self.db) as db:
            db.delete(self.table, where)

    def is_exist(self, where):
        r = self.query_one(where)
        if len(r) != 1:
            print(r)
            return False
        else:
            return True
