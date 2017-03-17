#encoding=utf8
import random

class treenode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


def add(tree, data):
    if tree is None:
        tree = treenode(data)
        return tree
    elif data > tree.data:
        tree.right = add(tree.right, data)
    elif data < tree.data:
        tree.left = add(tree.left, data)
    return tree

def middle_list(tree):
    if tree is not None:
        middle_list(tree.left)
        print(tree.data)
        middle_list(tree.right)

def hou_list(tree):
    if tree is not None:
        hou_list(tree.left)
        hou_list(tree.right)
        print(tree.data)

def first_list(tree):
    if tree is not None:
        print(tree.data)
        first_list(tree.left)
        first_list(tree.right)

def min_node(tree):
    if tree is not None:
        while tree.left is not None:
            tree = tree.left
        return tree.data

def add2(tree, data):
    if tree is None:
        return treenode(data)
    if data > tree.data:
        tree.right = add2(tree.right, data)
    if data < tree.data:
        tree.left = add2(tree.left, data)
    return tree
def delete_node(tree, data):
    if tree is None:
        print("空")
    elif data > tree.data:
        tree.right = delete_node(tree.right, data)
    elif data < tree.data:
        tree.left = delete_node(tree.left, data)
    elif tree.right is not None and tree.left is not None:
        min_data = min_node(tree.right)
        tree.data = min_data
        tree.right = delete_node(tree.right, min_data)
    else:
        if tree.left is None:
            tree = tree.right
        elif tree.right is None:
            tree = tree.left
    return tree

def delete_node2(tree, data):
    if tree is None:
        print("kong")
    elif data > tree.data:
        tree.right = delete_node2(tree.right, data)
    elif data < tree.data:
        tree.left = delete_node2(tree.left, data)
    elif tree.left is not None and tree.right is not None:
        min_data = min_node(tree.right)
        tree.data = min_data
        tree.right = delete_node2(tree.right, min_data)
    else:
        if tree.left is None:
            tree = tree.right
        elif tree.right is None:
            tree = tree.left
    return tree


def exchange_tree(root):
    if root.height % 2 == 0 and (root.left is not None or root.right is not None):
        root.right,root.left = root.left,root.right
    if root.left is not None:
        root.left.height = root.height + 1
        exchange_tree(root.left)
    if root.right is not None:
        root.right.height = root.height + 1
        exchange_tree(root.right)

def main():
    tree = treenode(25)
    ele_list = [3, 2, 45, 5, 23, 76, 4, 60, 80]
    for i in ele_list:
        # first_list(tree)
        add2(tree, i)
    # while tree.right is not None:
    #     # print(tree)
    #     print(tree.data)
    #     tree = tree.right
    first_list(tree)
    print("++++++++++++++++++++")
    delete_node2(tree, 60)
    delete_node2(tree, 80)
    first_list(tree)


    # exchange_tree(tree)
    # first_list(tree)
    # hou_list(tree)
    # first_list(tree)
    # print(min_node(tree))

        
    


if __name__ == '__main__':
    main()





# class Tree(object):
#     def __init__():
#         self.root = treenode()
#         self.myQueue = []
    
#     def add():



