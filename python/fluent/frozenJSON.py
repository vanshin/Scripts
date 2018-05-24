#coding=utf8

import keyword


class FrozenJSON(object):


    def __new__(cls, data):
        if isinstance(data, dict):
            return super().__new__(cls)
        elif isinstance(data, list):
            return [cls(i) for i in data]
        else:
            return data


    def __init__(self, mapping):
        self.__data = dict(mapping)
        for k,v in mapping.items():
            if keyword.iskeyword(k):
                self.__data[k+'_'] = v


    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        elif item not in self.__data:
            return None
        else:
            return FrozenJSON(self.__data[item])

def main():
    a = {'class': 12, 'bb': 13}
    fa = FrozenJSON(a)
    print(fa.class_)
    print(fa.bb)

if __name__ == '__main__':
    main()



