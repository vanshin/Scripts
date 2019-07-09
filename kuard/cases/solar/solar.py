from tester.kttp import HttpTester

class SolarBase(HttpTester):

    name = 'solar_api'

    ses_get_url = '/solar/v1/user/login'
    ses_del_url = '/solar/v1/user/logout'
    ses_data = {'username': '14000000000', 'password': 'qfpay123456'}

    def before_http_call(self):

        self._http_call()


