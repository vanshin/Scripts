from baseset import ThriftConnConf, BaseSet
from qfcommon3.thriftclient.apollo import ApolloServer
from qfcommon3.thriftclient.org import OrgServer

apollo_addr_156 = [{'addr': ('172.100.113.34', 6900), 'timeout': 5000}, ]
apollo_addr_107 = [{'addr': ('172.100.113.34', 6901), 'timeout': 5000}, ]

org_api_addr = [{'addr': ('172.100.113.34', 8010), 'timeout': 5000}, ]
org_api_addr_qa = [{'addr': ('172.100.101.107', 8009), 'timeout': 5000}, ]

apollo_156 = ThriftConnConf('apollo_156', apollo_addr_156, ApolloServer)
apollo_107 = ThriftConnConf('apollo_107', apollo_addr_107, ApolloServer)
org_api = ThriftConnConf('org_api', org_api_addr, OrgServer, True)
org_api_qa = ThriftConnConf('org_api_qa', org_api_addr_qa, OrgServer, True)

cli = BaseSet.from_obj(apollo_156)
cli.register_more(
    apollo_107,
    org_api,
    org_api_qa
)

class HttpConfig(object):
    pass

class OrgProtal(HttpConfig):
    HOST = '172.100.113.34'
    PORT = '8198'
    WITH_SSL = False



DATABASE = {
    'qf_core': {
        'engine': 'pymysql',
        'db': 'qf_core',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_user': {
        'engine': 'pymysql',
        'db': 'qf_user',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_solar': {
        'engine': 'pymysql',
        'db': 'qf_solar',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_mis': {
        'engine': 'pymysql',
        'db': 'qf_mis',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_qudao': {
        'engine': 'pymysql',
        'db': 'qf_qudao',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qmm_wx': {
        'engine': 'pymysql',
        'db': 'qmm_wx',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'honey_manage': {
        'engine': 'pymysql',
        'db': 'qmm_wx',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_risk_2': {
        'engine': 'pymysql',
        'db': 'qf_risk_2',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_trade': {
        'engine': 'pymysql',
        'db': 'qf_trade',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_fund2': {
        'engine': 'pymysql',
        'db': 'qf_fund2',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_audit': {
        'engine': 'pymysql',
        'db': 'qf_audit',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'wxmp_customer': {
        'engine': 'pymysql',
        'db': 'wxmp_customer',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_weifutong': {
        'engine': 'pymysql',
        'db': 'qf_weifutong',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'open_user': {
        'engine': 'pymysql',
        'db': 'open_user',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_settle': {
        'engine': 'pymysql',
        'db': 'qf_settle',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },
    'qf_org': {
        'engine': 'pymysql',
        'db': 'qf_qudao',
        'host': '172.100.101.156',
        'port': 3306,
        'user': 'qf',
        'passwd': '123456',
        'charset': 'utf8',
        'conn': 16,
    },

}
