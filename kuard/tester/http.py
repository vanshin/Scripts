
import copy
import redis
import random
import requests
import traceback

from prettytable import PrettyTable

from ..config.config_http import NameMap


class FieldStruct(object):

    def __init__(self, fields):
        self.fields = fields
        self.datas = {}

        # 准备error flag
        self.error_flags = {
            i.name: False for i in self.fields
            if i.is_must()
        }

    def reset_flag(flag_map, flag=False):
        for _, _flag in flag_map.items():
            _flag = flag


    def get_full_data(self):
        data = {}
        for field in self.fields:
            data[field.name] = field.data
        return data

    def one_must_error(self):
        for name, flag in self.error_flags:
            if flag == False:
                return name

    def __iter__(self):

        for name, flag in self.error_flags:
            data = self.get_full_data()
            data.pop(name)
            yield data

        yield self.get_full_data()

class HttpTester(object):

    AUTO_DEL = False
    CHECK_DB = False

    allow_method = ('get', 'post', 'put')

    def __init__(self):

        self.httper = requests
        if not config.WITH_SSL:
            self.host = 'http://' + config.HOST
        else:
            self.host = 'https://' + config.HOST
        self.host += ':' + config.PORT + self.url

        self.struct = FieldStruct(struct)

    def test_auto(self):
        for i in self.struct:
            ret = self.api_call(i)
            print(ret)

    def test(self):
        funcs = dir(self)

        test_funcs = []
        for i in funcs:
            if i.startswith('test_'):
                test_funcs.append(i)

        for i in test_funcs:
            getattr(self, i)()
            self.http_call()


    def auto_del(self, auto):
        self.AUTO_DEL = auto

    def check_db(self, check):
        self.CHECK_DB = check

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

    def __call__(self):
        pass

    def http_call(self, data):

        return self._http_call(self.method, data)

    def _http_call(self,
        method: str='get',
        data: dict=None,
        with_ses: bool=True,
        with_token: bool=False,
        fmt: str='default'
    ):
        '''调用http接口

        params:
            method: 方法
            data: 数据
            with_ses: cookie是否带上session
            with_token: 是否带上token
            fmt: 格式化返回方法
        return:
            基于fmt

        '''

        if method not in self.allow_method:
            raise ValueError

        cookies = {}
        header = {}
        data = {} if data is None else data
        if with_ses:
            cookies = {'sessionid': self.sessionid}
        if with_token:
            headers = {'token': self.token}

        func = getattr(self.httper, method)
        try:
            ret = func(self.host, data, headers={}, cookies={'sessionid': self.sessionid})
            ret = ret.json()
        except:
            print(traceback.format_exc())
        # 参数 实际返回 预定返回
        return ret

    def http_call(self):
        return self.api_call(self.data)

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


class SessionMixin(object):

    def __init__(self):

        redis_host = getattr(config, 'REDIS_HOST', '127.0.0.1')
        redis_port = getattr(config, 'REDIS_PORT', '6379')
        self.redis = redis.Redis(host=redis_host,port=redis_port)

        self.session_key = 'ktest_sessionid_{}'.format(self.name)

        self.sessionid = self.get_sessionid()
        if not self.sessionid:
            raise ValueError


    def _set_redis_sesid(self, value):
        self.redis.set(self.session_key, value)

    def _reset_redis_sesid(self):
        self.redis.set(self.session_key, '')

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


class WebTester(HttpTester):
    pass
