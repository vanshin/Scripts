import json

from config import cli as tcli

def main():

    content = {'userid': '2805527', 'src': 'org_salesman', 'sls_uid': '2803747'}

    ret = tcli.org_api.msgpass('mchnt_api.signup', json.dumps(content))
    print(ret)

if __name__ == '__main__':
    main()

