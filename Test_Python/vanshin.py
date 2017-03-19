import os
def deco(func):
    print("123")
    def warpper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return warpper

@deco
def myfunc(parameter):
    print("run with %s" % parameter)
myfunc("aa")

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

patha = "d://tmp"
print_directory_contents(patha)