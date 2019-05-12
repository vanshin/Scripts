
import copy
import redis
import random
import config
import requests
import traceback

from prettytable import PrettyTable


class FieldDescriptor(object):

    _all_status = ('exist', ' must')
    _all_ftype = ('int', 'str')

    def __init__(self, status, ftype, name):

        self.stats = status
        self.ftype = ftype
        self.name = name

    @classmethod
    def from_struct(cls, s, name):
        '''exist.int: name'''

        # 确保数据完整
        s = str(s).split('.')
        if len(s) != 2:
            raise ValueError
        if (s[0] not in _all_status) or (s[1] not in _all_ftype):
            raise ValueError

        # 实例化
        return cls(s[0], s[1], name)

class StructData(object):

    def __init__(self, sttd):
        self.attrs = {}
        self.data = {}
        self.parse(sttd)

    def parse(self, sttd):
        for k,v in sttd.items():
            k = TestAttr(k)
            self.attrs[k.name] = k.status
            self.data[k.name] = random.choice(v)

    def __iter__(self):
        ret_code = '2101'
        yield ({}, ret_code, '空数据')
        for k,v in self.attrs.items():
            _data = copy.deepcopy(self.data)
            if self.attrs[k] != 'must':
                continue
            _data.pop(k)
            yield (_data, ret_code, '必须参数缺少{}'.format(k))
        yield (self.data, '0000', '有效数据验证')



class HttpTester(object):

    AUTO_DEL = False
    CHECK_DB = False

    def __init__(self):

        self.httper = requests
        redis_host = getattr(config, 'REDIS_HOST', '127.0.0.1')
        redis_port = getattr(config, 'REDIS_PORT', '6379')
        self.redis = redis.Redis(host=redis_host,port=redis_port)
        self.session_key = 'ktest_sessionid_{}'.format(self.name)
        if not config.WITH_SSL:
            self.host = 'http://' + config.HOST
        else:
            self.host = 'https://' + config.HOST
        self.host += ':' + config.PORT + self.url
        self.sessionid = self.get_sessionid()
        if not self.sessionid:
            raise ValueError

    def get_sessionid(self):
        try:
            if not hasattr(self, 'ses_data'):
                return None
            sesid = self.redis.get(self.session_key)
            if sesid:
                self._set_redis_sesid(sesid)
                return sesid.decode('utf8')
            host = 'http://'+config.HOST+':'+config.PORT+self.ses_get_url
            ret = self.httper.post(host, self.ses_data)
            ret = ret.json()
            ret_data = ret.get('data') or {}
            if 'sessionid' in ret_data:
                self._set_redis_sesid(ret_data['sessionid'])
                return ret_data['sessionid']
            return None
        except:
            print(traceback.format_exc())

    def auto_del(self, auto):
        self.AUTO_DEL = auto

    def check_db(self, check):
        self.CHECK_DB = check

    def _set_redis_sesid(self, value):
        self.redis.set(self.session_key, value)

    def _reset_redis_sesid(self):
        self.redis.set(self.session_key, '')

    def fmt_ret(self, params, ret, pre_code):
        respcd = ret['respcd']
        data = ret['data']
        sign = '*'
        print(sign*50)
        print('params:')
        print(params)
        print('expect code: {}, ret code: {}'.format(pre_code, respcd))
        if self.api_type == 'list':
            if not data['list']:
                print('no data')
                print(sign*50)
                return
            x = PrettyTable()
            x.field_names = list(data['list'][0].keys())
            for i in data['list']:
                x.add_row(list(i.values()))
            print('return data:')
            print(x)
        else:
            print('return data:')
            print(data)

    def api_call(self, data=None):
        if not data:
            data = {}
        http_method = getattr(self.httper, self.method, 'get')
        try:
            ret = http_method(self.host, data, cookies={'sessionid': self.sessionid})
            ret = ret.json()
        except:
            print(traceback.format_exc())
        # 参数 实际返回 预定返回
        return ret

    def http_call(self):
        return self.api_call(self.data)

    def is_0000(self, ret):
        if ret['respcd'] != '0000':
            return False
        return True

    def _test_list(self):
        all_datas = [{}]
        full_data = {}
        for k,v in self.sttd.items():
            one_data = {}
            k = TestAttr(k)
            one_data[k.name] = random.choice(v)
            full_data[k.name] = random.choice(v)
            all_datas.append(one_data)
        for i in all_datas:
            ret = self.api_call(i)
            if not self.is_0000(ret):
                print('test api_type {} failed, return {}'.format(
                    self.api_type, ret.get('respcd')))

    def _test_create(self):
        datas = StructData(self.sttd)
        for data, pre_code, descr in datas:
            self.api_call(data)
            db_check_desc = ''
            if self.CHECK_DB:
                table = Tabler.from_info(self.db_info)
                if table.is_exist(data):
                    db_check_desc = '成功-数据库存在'
                else:
                    self.auto_del(False)
                    db_check_desc('失败-数据库不存在')
            if self.AUTO_DEL:
                table = Tabler.from_info(self.db_info)
                table.del_one(data)

    def _test_update(self):
        datas = StructData(self.sttd)
        for data, pre_code in datas:
            self.api_call(data, pre_code)

    def test_auto(self):
        pass

    def test(self):
        funcs = dir(self)

        test_funcs = []
        for i in funcs:
            if i.startswith('test_'):
                test_funcs.append(i)

        for i in test_funcs:
            getattr(self, i)()
            self.http_call()


