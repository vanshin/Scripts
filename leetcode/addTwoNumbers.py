# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def addTwoNumbers(l1, l2):
    pass
def addTwoNumbers2(l1, l2):
    n = 0
    m = 0
    l1_num = 0
    l2_num = 0
    result_list = []
    while l1 is not None:
        l1_num = l1_num + l1.val * 10**n
        n = n + 1
        l1 = l1.next
    while l2 is not None:
        l2_num = l2_num + l2.val * 10**m
        m = m + 1
        l2 = l2.next
    sum = l1_num + l2_num
    sum_str = str(sum)
    for item in sum_str[::-1]:
        result_list.append(ListNode(item))
    for index in range(len(result_list)):
        if index + 1 == len(result_list):
            result_list[index].next = None
        else:
            result_list[index].next = result_list[index+1]
    return result_list[0]
def main():
    tj1_list = []
    tj2_list = []
    one = ListNode(1)
    eight = ListNode(8)
    one.next = eight
    zero = ListNode(2)
    five = ListNode(4)
    zero.next = five
    res = addTwoNumbers2(one, zero)
    for i in range(100):
        print(res.val)
        res = res.next
    # for i in range(3):
    #     tmp = ListNode(i + 2)
    #     tmp2 = ListNode(i + 3)
    #     tj1_list.append(tmp)
    #     tj2_list.append(tmp2)
    
    # for index in range(len(tj1_list)):

    #     if index < 2:
    #          tj1_list[index].next = tj1_list[index+1]
    #          tj2_list[index].next = tj2_list[index+1]
    #     else:
    #         tj1_list[index].next = None
    #         tj2_list[index].next = None
    # result = addTwoNumbers(tj1_list[0], tj2_list[0])
    # result = addTwoNumbers(one, zero)
    # print(result[0].next.val)
    
    # while result is not None:
    #     print(result.val)
    #     result = result.next
    
    

    

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
            