from .solar import SolarBase

class GetOrgList(SolarBase):

    method = 'get'
    url = '/org/user/list'
    struct = {
        'status': 'exist.int',
        'qd_uid': 'exist.int'
    }


class CreateMpconfInfo(SolarBase):

    url = '/solar/v1/oper/mpconf/info'
    method = 'post'

    sttd = {
        'must.int.confmodel': [2,1],
        'must.int.belong': [0,1,2,],
        'must.int.chnlcode': [3,14],
        'must.str.main': ['main_test'],
        'must.str.cid': ['cidtest'],
        'must.str.pay_appid': ['payappidtest'],
        'must.str.menu': ['menu_test'],
        'maybe.str.appid': ['appid_test'],
        'maybe.str.appname': ['appname_test'],
        'exist.str.appkey': ['appkey_test'],
        'exist.str.uid': ['123,234']
    }

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

