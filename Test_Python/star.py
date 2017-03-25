#encoding=utf8
# if sys.version_info[0] == 2:
from __future__ import print_function
import random
import sys

class star(object):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y





class Board(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.start = 0
        self.storage = [[star(random.randint(0,3), x, y) for y in range(5)] for x in range(5)]

    def get_star(self, x, y):
        if x > self.length or x < self.start or y < self.start or y :
            raise IndexError("chao chu changdu")
        try:
            return self.storage[x][y]
        except Exception as identifier:
            print(identifier)
        


def get_stor():
    stor = [[star(random.randint(1,4), x, y) for y in range(5)] for x in range(5) ]
    return stor

def delete_zero(stor):
    zero_col = []
    for i in stor:
        sum = 0
        for j in i:
            sum = j.color + sum
        if sum == 0 and j.x < 4:
            zero_col.append(j.x)
    zero_col.sort()
    for i in zero_col:
        stor = delete_col(i, stor)


def delete_col(col, stor):
    for item in range(col, 4):
        for i in range(5):
            stor[item][i].color = stor[item+1][i].color
    for i in range(5):
        stor[4][i].color = 0
    return stor


def touch_one2(location, stor, yl_stars):
    a, b = location
    # if yl_location is not None:
    #     yl_star = []
    #     for i in yl_location:
    #         y_a, y_b = i
    #         yl_star.append(stor[y_a][y_b])
    location_star = stor[a][b]
    location_color = location_star.color
    a_round = []
    b_round = []
    if 0 <= b-1 < 5:
        a_round.append(b-1)
    if 0 <= b+1 < 5:
        a_round.append(b+1)
    if 0 <= a+1 < 5:
        b_round.append(a+1)
    if 0 <= a-1 < 5:
        b_round.append(a-1)
    tmp = []
    for rb in a_round:
        if stor[a][rb].color == location_color:
            tmp.append(stor[a][rb])
    for ra in b_round:
        if stor[ra][b].color == location_color:
            tmp.append(stor[ra][b])
    for star in yl_stars:
        if star in tmp:
            tmp.remove(star)
    if len(tmp) > 0:
        for st in tmp:
            yl_stars.append(location_star)
            tmp = tmp + touch_one2((st.x, st.y), stor, yl_stars)
    else:
        return tmp
    return tmp


def touch_one(location, stor, yl_location=None):
    a, b = location
    if yl_location is not None:
        y_a, y_b = yl_location
        yl_star = stor[y_a][y_b]
    location_star = stor[a][b]
    location_color = location_star.color
    a_round = []
    b_round = []
    if 0 <= b-1 < 5:
        a_round.append(b-1)
    if 0 <= b+1 < 5:
        a_round.append(b+1)
    if 0 <= a+1 < 5:
        b_round.append(a+1)
    if 0 <= a-1 < 5:
        b_round.append(a-1)
    tmp = []
    for rb in a_round:
        if stor[a][rb].color == location_color:
            tmp.append(stor[a][rb])
    for ra in b_round:
        if stor[ra][b].color == location_color:
            tmp.append(stor[ra][b])
    if yl_location is not None and  yl_star in tmp:
        tmp.remove(yl_star)
    if len(tmp) > 0:
        for st in tmp:
            tmp = tmp + touch_one((st.x, st.y), stor, yl_location=location)
    else:
        return tmp
    return tmp

def main():
    stor = get_stor()
    show_stor(stor)
    # keep_del(stor)
    while True:
        if sys.version_info[0] == 3:
            tmp = input("num: ")
        elif sys.version_info[0] == 2:
            tmp = raw_input("num: ")
        a, b = tmp.split(",")
        a = int(a)
        b = int(b)
        li = touch_one2((a,b), stor,[])
        li.append(stor[a][b])
        li = list(set(li))
        li = sort_del(li)
        for i in li:
            print("li_so:",i.x,i.y)
        if len(li) > 1:
            for i in li:
                lo = (i.x, i.y)
                stor = delete(lo, stor)
        delete_zero(stor)
        show_stor(stor)



def keep_del(stor):
    while True:
        tmp = input("num:")
        a, b = tmp.split(",")
        a = int(a)
        b = int(b)
        stor = delete((a, b), stor)
        show_stor(stor)

def sort_del(result):
    y_sort = []
    new_result = []
    for i in result:
        y_sort.append(i.y)
    y_sort.sort()
    y_sort = set(y_sort)
    for y in y_sort:
        for star in result:
            if star.y == y:
                new_result.append(star)
    return new_result


def delete(location, stor):
    a, b = location
    stor[a][b].color = 0
    tmp = []
    for i in range(b-1,-1,-1):
        tmp.append(stor[a][i].color)
    tmp.append(0)
    for j in range(b,-1,-1):
        stor[a][j].color = tmp[b-j]
    return stor

def show_stor(stor):
    for i in range(len(stor[0])):
        for j in range(len(stor)):
            if j == 4:
                print(stor[j][i].color)
            else:
                print(stor[j][i].color,end='')

if __name__ == '__main__':
    main()
