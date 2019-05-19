from dataclasses import dataclass

@dataclass
class ServConf(object):

    host: str = '172.100.113.34'
    port: str
    base_url: str = ''
    with_ssl: bool = False


class NameMap(object):

    nmap = {
        'solar_api': ServConf(post='2990', base_url='/solar/v1'),
    }


