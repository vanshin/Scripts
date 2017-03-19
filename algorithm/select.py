# encoding=utf8
import timeit
import random
def max_k(a):
    k = len(a)//2
    for index in range(k):
        for rest in range(index+1, len(a)):
            if a[index] < a[rest]:
                a[index], a[rest] = a[rest], a[index]
    return a[k-1]

def max_k2(a, k):
    if len(a) == 0:
        return "shuruweikong"

    result, index = paixu(a)
    if index == k:
        return result[k]
    elif k < index:
        return max_k2(result[0:index], k)
    elif k > index:
        return max_k2(result[index+1:], k-index-1)

def paixu(a):
    p = a[0]
    left = []
    right = []
    for item in a[1:]:
        if item <= p:
            left.append(item)
        elif item > p:
            right.append(item)
    index = len(left)
    return left+[p]+right, index

def get_test():
    test = []
    for i in range(8):
        j = random.random() * 10
        test.append(j)
    return test

def shuchu():
    print("123")

def main():
    test = [5, 25, 7, 2, 4, 8, 34, 76, 23]
    # test2 = [5, 4, 7, 2, 3, 8]
    k = len(test)//2
    
    new_k = len(test) - k
    namespace = {
        "test2":get_test(),
        "max_k2":max_k2
    }
    t = timeit.Timer("max_k2(get_test(), 5)", globals=globals())
    print(t.timeit(1000))
    

    # print(timeit.timeit("max_k(get_test())","from __main__ import max_k;from __main__ import get_test"))
    # print(max_k2(test, new_k))
    # print(max_k(test))

if __name__ == '__main__':
    main()
