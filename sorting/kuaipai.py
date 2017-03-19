def kuaipai(a):
    flag = a[0]
    left = []
    right = []
    for i in a:
        if i >= flag:
            right.append(i)
        elif i < flag:
            left.append(i)
    return kuaipai(left) + flag + kuaipai(right)
            


def qsort(L):  
    if len(L) <= 1: return L  
    return qsort([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + qsort([ge for ge in L[1:] if ge >= L[0]])  

def insert_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        tmp = l[i]
        l[i] = l[min_index]
        l[min_index] = tmp
    print("insert_sort success!!!")




def qsort2(a):
    if len(a) <= 1:
        return a
    return qsort2([x for x in a[1:] if x < a[0]]) + [a[0]] + qsort2([x for x in a[1:] if x > a[0]])


# def charu(a):
#     for i in range(len(a)):
#         index = i
#         for j in range(i+1,len(a)):
#             if a[index] > a[j]:
                

def main():
    a = [7,43,45,68,65,42,3,5,63,4,24,2]
    t = qsort2(a)
    print "1111111111111111111"
    # charu(a)
    print t

if __name__ == '__main__':
    main()