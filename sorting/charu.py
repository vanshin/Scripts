

# def insertpai(a):
#     for i in range(1,len(a)):
#         tmp = a[i]
#         point = i
#         for j in range(i,0,-1):
#             if a[j-1] > tmp:
#                 a[j] = a[j-1]
#                 point = point - 1
#         a[point] = tmp





def insertpai2(a):
    for i in range(1,len(a)):
        tmp = a[i]
        point = i
        for j in range(i,0,-1):
            if a[j-1] > tmp:
                a[j] = a[j-1]
                point = point - 1
        a[point] = tmp
    return a

def shellSort(seq):  
    


def ceshi():
    for j in range(5,0,-1):
        print j

def main():
    # ceshi()
    a = [7, 4, 5, 26, 14, 78, 234]
    insertpai2(a)
    print a


if __name__ == '__main__':
    main()