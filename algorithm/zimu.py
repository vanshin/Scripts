
# def set_zimu():
#     pass

def test(a):
    a = 100
    print a
    print locals()

def test_li(li=[]):
    li.append(20)
    print li
    print id(li)
    print locals()

def main():
    # a = 90
    # test(20)
    li = [1, 2, 3]
    for i in range(10):
        test_li()
    # print id(li)
    # print locals()

if __name__ == '__main__':
    main()

