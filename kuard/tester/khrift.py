
import sys
sys.path.append('/home/vanshin/code/')


import json
import traceback
import logging

from dataclasses import dataclass
from typing import Any

from thrift.Thrift import TException
from qfcommon3.server.client import ThriftClient
from qfcommon3.thriftclient.apollo.ttypes import ApolloException

from util.excepts import ThirdError, ServerError, ParamError

log = logging.getLogger()

DEFAULT = 1
KEEP_CONN = 2

@dataclass
class ThriftConnConf(object):

    name: str
    addrs: list
    thrift_mod: Any
    framed: bool = False
    timeout: int = 0
    raise_except: bool = True

class BaseSet(object):

    def __init__(self, addrs, thrift_mod, framed=False):

        default_config_obj = ThriftConnConf('default', addrs, thrift_mod, framed)

        # 各种模式
        self.run_mode = DEFAULT

        # 连接配置
        self.thrift_conn_confs = {
            'default': {
                'config': default_config_obj,
                'keep_conn': None
            }
        }

    def __getattr__(self, func_name):

        # 已经注册的服务直接返回client
        if self.is_registered(func_name):
            cli = self._get_cli(func_name)
            # 行为一致,展示参数
            call_closure = getattr(cli.call, '__closure__', None) # 防止重复
            if call_closure is None:
                cli.call = with_log(cli.call)
            return cli

        # 默认服务的调用
        def _(*args, **kwargs):
            try:
                default_cli = self._get_cli('default')
                log.info(f'func={func_name}|args={args}|kwargs={kwargs}')
                return default_cli.call(func_name, *args, **kwargs)
            except ApolloException as e:
                log.warn(traceback.format_exc())
                raise ThirdError('用户服务错误,{}'.format(e.respmsg))
            except TException as e:
                log.warn(traceback.format_exc())
                raise ThirdError('内部服务错误,{}'.format(e))
            except:
                log.warn(traceback.format_exc())
                raise ThirdError('内部错误')
        return _

    def __enter__(self):
        self._with_flag = True

    def __exit__(self, exc_type, exc_value, traceback):
        self._with_flag = False
        self._exit_func()

    def __str__(self):
        addr = ';'.join([f"{i['addr'][0]}:{i['addr'][1]}" for i in self.addr])
        thrift_name = self.thrift.__name__.split('.')[-1]
        return f'<{self.__class__.__name__} with {thrift_name} on {addr}>'

    def __repr__(self):
        return self.__str__()


    def _value_from_confs(self, name, key):
        '''从保存的配置中加载指定的连接配置'''

        if name not in self.thrift_conn_confs:
            raise ParamError('未注册指定的服务')

        item = self.thrift_conn_confs[name]
        value = item.get(key)

        if key == 'config' and not isinstance(value, ThriftConnConf):
            raise ParamError('注册的服务配置错误')

        return value

    def _value_to_confs(self, name, key, value):

        if name not in self.thrift_conn_confs:
            raise ParamError('未注册指定的服务')

        item = self.thrift_conn_confs[name]

        if key == 'config' and not isinstance(value, ThriftConnConf):
            raise ParamError('注册的服务配置实例错误')

        item[key] = value

    def _thrift_name(self, thrift):
        '''获取thrift服务的名字'''
        return thrift.__name__.split('.')[-1]

    def _build_cli(self, config_obj):
        '''根据ThriftConnConf创建连接'''

        try:
            thrift_cli = ThriftClient(
                config_obj.addrs,
                config_obj.thrift_mod,
                timeout=config_obj.timeout,
                framed = config_obj.framed,
                raise_except = config_obj.raise_except,
            )
        except:
            log.warn(traceback.format_exc())
            raise ThirdError('无法建立和服务的链接')

        return thrift_cli

    def _get_cli(self, name):
        '''根据运行模式来返回连接实例'''

        if self.run_mode == KEEP_CONN:

            # 只允许上下文管理器使用保持连接
            if self._with_flag is False:
                raise ServerError('请使用上下文管理来启用连接保持')

            keep_conn = self._value_from_confs(name, 'keep_conn')

            if keep_conn is None:
                config_obj = self._value_from_confs(name, 'config')
                keep_conn = self._build_cli(config_obj)
                self._value_to_confs(name, 'keep_conn', keep_conn)

            return keep_conn

        elif self.run_mode == DEFAULT:
            config_obj = self._value_from_confs(name, 'config')
            return self._build_cli(config_obj)

    def keep_conn(self):
        '''保持连接'''

        self.run_mode = KEEP_CONN
        self._exit_func = self._keep_conn_exit
        return self

    def _keep_conn_exit(self):
        '''退出保持连接'''

        # log.info('exit conn keep')
        self.run_mode = DEFAULT

        # 回收所有的keep_conn
        for k,v in self.thrift_conn_confs.items():
            if v.get('keep_conn') is not None:
                v['keep_conn'] = None

    def is_registered(self, name):
        if name in self.thrift_conn_confs:
            return True
        return False

    def register(self, config_obj):
        '''注册其他thrift 连接'''

        if not isinstance(config_obj, ThriftConnConf):
            raise ParamError('注册服务失败，不是指定的Thrift连接实例')

        item = {
            'config': config_obj,
            'keep_conn': None
        }

        self.thrift_conn_confs[config_obj.name] = item

    def register_more(self, *configs):

        for i in configs:
            self.register(i)

    @classmethod
    def from_obj(cls, config_obj):
        '''快捷实例化'''

        if not isinstance(config_obj, ThriftConnConf):
            raise ParamError('注册服务失败，不是指定的Thrift连接实例')

        return cls(
            config_obj.addrs,
            config_obj.thrift_mod,
            config_obj.framed
        )


def with_log(func):
    def _(name, *args, **kw):
        # print(f'func={name}|args={args}|kwargs={kw}')
        log.info(f'func={name}|args={args}|kwargs={kw}')
        return func(name, *args, **kw)
    return _

if __name__ == '__main__':

    print('kk')
    from qfcommon3.thriftclient.apollo import ApolloServer

    APOLLO_SERVERS = [{'addr': ('172.100.113.34', 6900), 'timeout': 5000}, ]

    print('kk')
    tcc = ThriftConnConf('apollo', APOLLO_SERVERS, ApolloServer)
    userset = BaseSet.from_obj(tcc)
    # userset.register(tcc)

    ret = userset.user_edit(json.dumps({'userid': '11327', 'licensestat_date': '2019-12-12'}))
    print('kk')
    print(ret)

    # with userset.keep_conn():
        # ret = userset.apollo.ping()
        # ret = userset.apollo.ping()
