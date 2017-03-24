#encoding=utf8

import random

class star(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
class Board(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.storage = [[star(random.randint(0,3), x, y) for y in range(5)] for x in range(5)]

    def 

def get_stor():
    stor = [[star(random.randint(0,3), x, y) for y in range(5)] for x in range(5) ]
    return stor



def touch_one(location, stor, yl_location=None):
    a, b = location
    if yl_location is not None:
        y_a, y_b = yl_location
        yl_star = stor[y_a][y_b]
    location_star = stor[a][b]
    location_color = location_star.color
    a_round = [b-1, b+1]
    b_round = [a-1, a+1]
    tmp = []
    for rb in a_round:
        if stor[a][rb].color == location_color:
            tmp.append(stor[a][rb])
    for ra in b_round:
        if stor[b][ra].color == location_color:
            tmp.append(stor[b][ra])
    if yl_location is not None and yl_star in tmp:
        tmp.remove(yl_star)
    for st in tmp:
        if st is None:
            tmp.remove(st)
    for st in tmp:
        tmp.append(touch_one((st.x, st.y), stor, yl_location=location))
    if len(tmp) == 0:
        return None
    tmp.append(location_star)
    print("123123")
    print(tmp)
    return tmp

def main():
    # stor = get_stor()
    # for i in stor:
    #     print("----")
    #     for j in i:
    #         print(j.color)
    # print(touch_one((2,2),stor))



if __name__ == '__main__':
    main()