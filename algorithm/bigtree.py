import random
class treenode():
    
    def __init__(self, data):
        self.data = data
        self.next = list()

    def insert_child(self, child):
        """ 插入一个treenode或者需要保存的数据 """
        if isinstance(child, treenode):
            self.next.append(child)
        else:
            tmp_treenode = treenode(child)
            self.next.append(tmp_treenode)

    def get_child_node_num(self):
        """ 拿到所有节点的数量 """
        child_list = self.next
        num = 1
        if len(self.next) == 0:
            return 1
        for child in child_list:
            num = num + child.get_all_child_node()
        return num
    
    


    
def main():
    top = treenode(30)
    
    for i in range(4):
        top.insert_child(i)
    for j in top.next:
        j.insert_child(42)
        j.insert_child(34)
    
    print(top.get_all_child_node())
            
    

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))

