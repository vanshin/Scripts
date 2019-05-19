from tester import Tester

class SolarBase(Tester):

    name = 'solar_api'

    ses_get_url = '/solar/v1/user/login'
    ses_del_url = '/solar/v1/user/logout'
    ses_data = {'username': '14000000000', 'password': 'qfpay123456'}


