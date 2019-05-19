from .solar import SolarBase

from ...util import Int, Str

class GetOrgList(SolarBase):

    method = 'get'
    url = '/org/user/list'
    struct = {
        'status': 'exist.int',
        'qd_uid': 'exist.int'
    }

    def test_list(self):
        self.data = {
            'status': 1,
            'qd_uid': 11327
        }


class CreateMpconfInfo(SolarBase):

    url = '/solar/v1/oper/mpconf/info'
    method = 'post'
    datatype = 'form'

    struct = [
        Str('cid', 'must', const=(1,2,3)),
        Str('uid', 'any'),
        Str('main', 'must'),
        Str('menu', 'must'),
        Str('appid', 'maybe', const={'confmodel':1}),
        Str('appkey', 'exist'),
        Int('belong', 'must'),
        Int('chnlcode', 'must'),
        Int('confmodel', 'rely', const=(1,2)),
        Str('pay_appid', 'must'),
    ]


    def test_model_err(self):
        self.case = {
            'confmodel': '1',
            'appid': ['kkk', '', ''],
            'appname': ['', 'kkk', ''],
        }

        self.expect_code = '2102'

    def test_uid_err(self):
        self.case = {
            'uid': ['kk,34', '34,kkk', '213.34']
        }

        self.expect_code = '2102'

    def test_model_succ(self):
        self.auth_del(True)
        self.expect_code = '0000'
        self.check_db(True)

        self.case = {
            'confmodel': '2',
            'appid': ['kkk', '', ''],
            'appname': ['', 'kkk', ''],
        }

def main():

    kt = CreateMpconfInfo()
    kt.test()

if __name__ == '__main__':
    main()

