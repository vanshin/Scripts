class aa(object):
    def __init__(self, data):
        self.data = data

    def test(self):
        def wapr(f):
            print("1")
            print(f.vi)
            return f
        return wapr




aa = aa(44)
@aa.test()
def qq():
    vi = "vi"
    print(221)

qq()    


