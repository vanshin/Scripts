from dataclasses import dataclass

@dataclass
class ServConf(object):

    port: str
    host: str = '172.100.113.34'
    base_path: str = ''
    with_ssl: bool = False


class NameMap(object):

    nmap = {
        'solar_api': ServConf(port='2990', base_path='/solar/v1'),
    }


