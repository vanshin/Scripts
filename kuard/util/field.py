
import uuid
import random

from typing import Any, Iterable

class Field(object):

    _all_need = ('must', 'any', 'maybe')

    def __init__(self, name: str, need: str, const: Any=None):
        self.need = need
        self.name = name
        self.const = const

    def to_data(self):
        pass

    @property
    def _rs(self, num=4):
        return uuid.uuid4().hex[:num]

class Str(Field):


    def to_data(self, flag=False):

        if self.const is None:
            return f'kt_{self.name}_{self._rs}'

        if isinstance(self.const, Iterable):
            return random.choice(self.const)

        if isinstance(self.const, callable):
            return self.const()


def Int(Field):

    def to_data(self):
        pass
