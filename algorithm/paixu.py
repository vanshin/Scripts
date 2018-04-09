def kuaipai(list_p):
    # if len(list_p) == 1:
    #     return list_p
    p = list_p[0:1]
    return kuaipai([x for x in list_p[1:] if x < p]) + p + kuaipai([x for x in list_p[1:] if x > p])

def max(a):
    b = a[::-1]
    return b[2] 

# class treenode():
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

# def add(tree, data):
#     if tree is None:
#         a = treenode(data)
#         return a
#     if data > tree.data:
#         tree.right = add(tree.right, data)
#     if data < tree.data:
#         tree.left = add(tree.left, data)


# def left_tree(tree):
#     if tree is not None:

#         left_tree(tree.left)
#         print(tree.data)
#         left_tree(tree.right)

def delete(a):
    for i in range(len(a)):
        if a[i] in a[i+1:]:
            print(a[i])

def main():
    a = [4,3,7,9,8,4]
    # print(kuaipai(a))
    delete(a)

   
if __name__ == '__main__':
    main()
