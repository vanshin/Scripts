# encoding=utf8
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

def main():
    test = [5, 25, 7, 2, 4, 8, 34, 76, 23]
    test2 = [5, 4, 7, 2, 3, 8]
    k = len(test)//2
    new_k = len(test) - k
    print(max_k2(test, new_k))

if __name__ == '__main__':
    main()
