from .solar import SolarBase

class GetProList(SolarBase):

    url = '/solar/v1/utils/province/list'
    method = 'get'
    api_type = 'list'

    sttd = {
        'exist.int.area_no': [11,12,13],
    }

class GetCityList(SolarBase):

    url = '/solar/v1/utils/city/list'
    method = 'get'
    api_type = 'list'

    sttd = {
        'exist.int.area_id': [11,12,13],
    }

def main():

    kt = GetProList()
    kt2 = GetCityList()
    kt.test()
    kt2.test()

if __name__ == '__main__':
    main()

