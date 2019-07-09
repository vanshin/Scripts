
import json
import uuid
import redis
import random
import requests
import traceback

from typing import Any, Iterable, Callable
from prettytable import PrettyTable

from config.config_http import NameMap, BaseConf

class Field(object):

    _all_need = ('must', 'any', 'maybe', 'rely')

    def __init__(self, name: str, need: str, const: Any=None):
        self.need = need
        self.name = name
        self.const = const

    @property
    def data(self):
        pass

    def to_data(self):
        '''随机可用参数'''

        if self.const is None:
            return self.data

        if isinstance(self.const, tuple):
            print(self.const)
            return random.choice(self.const)

        if isinstance(self.const, Callable):
            return self.const()

    @property
    def wrong(self):
        if self.need == 'must':
            return None
        if self.need == 'any':
            return self._r_data()
        if self.need == 'maybe':
            if isinstance(self.const, dict):
                self.const[self.name] = None
                return self.const
        if self.need == 'rely':
            return self

    @property
    def correct(self):
        return self.to_data()

class Str(Field):

    def _rs(self, num=4):
        return uuid.uuid4().hex[:num]

    @property
    def data(self):
        if self.const is None:
            return f'kt_{self.name}_{self._rs()}'

class Int(Field):

    @property
    def data(self):
        return random.randint(1,10000)


class FieldStruct(object):

    def __init__(self, fields):
        self.fields = fields

    def get_full_data(self):
        data = {}
        for field in self.fields:
            data[field.name] = field.correct
        return data

    def __iter__(self):

        for i in self.fields:
            data = self.get_full_data()
            if isinstance(i.wrong, dict):
                data.update(i.wrong)
                yield data, False
            elif isinstance(i.wrong, Iterable):
                for i in i.wrong:
                    data[i.name] = i.wrong
                    yield data, False
            else:
                data[i.name] = i.wrong
                yield data, False

        yield self.get_full_data(), True

class HttpTester(object):

    allow_method = ('get', 'post', 'put')

    def __init__(self):

        self.httper = requests
        self.struct = FieldStruct(self.struct)
        self.load_conf()
        self.format_host()
        self.make_storer()

    def load_conf(self):
        if self.name not in NameMap.nmap:
            raise ValueError('无此配置文件')
        self.app_config = NameMap.nmap[self.name]
        self.config = BaseConf
        self.config.cookie_key = f'http_tester:{self.name}:cookie'
        self.config.header_key = f'http_tester:{self.name}:header'

    def http_call(self, data):

        self.before_http_call()

        ret = self._http_call(
            data=data,
            method=self.method,
            datatype=self.datatype
        )

        self.after_http_call()

        return ret

    def before_http_call(self):
        '''before hock'''
        pass

    def after_http_call(self):
        '''after hock'''
        pass

    def get_cookies(self):
        pass

    def _http_call(self,
        method: str='get',
        data: dict=None,
        datatype: str='json',
        fmt: str='default'
        headers: dict=None,
        cookies: dict=None,
    ):
        '''调用http接口

        准备header cookie

        params:
            method: 方法
            data: 数据
            datatype: 数据封装方式
            fmt: 格式化返回方法
        return:
            基于fmt

        '''

        if method not in self.allow_method:
            raise ValueError('不被允许的http method')

        # 准备数据
        data = {} if data is None else data
        headers = {} if headers is None else headers
        cookies = {} if cookies is None else cookies
        cookies.update(self.get_cookies())

        if datatype == 'json':
            headers['content-type'] = 'application/json'
            data = json.dumps(data)

        # 调用
        func = getattr(self.httper, method)
        try:
            ret = func(self.host, data, headers=headers, cookies=cookies)
        except:
            print(traceback.format_exc())

        return self.format_response(fmt, ret)

    def format_host(self):
        '''格式化host'''

        self.scheme = 'http' if not self.app_config.with_ssl else 'https'
        self.host = self.app_config.host
        self.port = self.app_config.port
        self.base_path = self.app_config.base_path

        self.base_url = f'{self.scheme}://{self.host}:{self.port}/{self.base_path}'

    def make_storer(self):
        self.storer = redis.Redis(self.http_config.redis_conf)

    def test_auto(self):
        for data, rtype in self.struct:
            ret = self.http_call(data)
            print(ret)

    def test_customize(self, name=None):
        funcs = dir(self)

        if name:
            test_func = getattr(self, 'test_'+name)
            ret = test_func()
            return ret

        test_funcs = []
        for i in funcs:
            if i.startswith('test_'):
                test_funcs.append(i)

        for i in test_funcs:
            getattr(self, i)()
            self.http_call()


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


    def format_data(self, datatype, data):
        pass

    def format_response(self, fmt, ret):
        if fmt == 'default':
            return ret



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


if __name__ == '__main__':
    pass
