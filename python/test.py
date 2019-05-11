
def aa(kk,kkk,kkka):
    def dect(*args):
        print(args)
        print('dect')
    return dect

# @aa(1,2,3)
def test():
    print('test')


aa(1,2,3)(test)
