import defines

class BaseError(Exception):

    def __init__(self, mess, code=defines.FAIL):
        self.mess = mess
        self.code = code

    def __str__(self):
        return '<code:{} mess:{}>'.format(self.code, self.mess)
