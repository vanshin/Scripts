from .solar import SolarBase


class GetTagList(SolarBase):

    url = '/solar/v1/oper/tag/list'
    method = 'get'
    api_type = 'list'

    sttd = {
        'exist.int.userid': [11327],
        'exist.str.content': ['测试'],
        'exist.str.tag_name': ['77520e18ce22']
    }

    yu = {
        'userid': ()
    }

def main():

    kt = GetTagList()
    kt.test()

if __name__ == '__main__':
    main()

