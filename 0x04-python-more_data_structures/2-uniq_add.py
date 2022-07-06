#!/usr/bin/python3
def uniq_add(mylist=[]):
    uniq_list = []
    sum = 0
    for i in mylist:
        if i not in uniq_list:
            uniq_list.append(i)
            sum += i
    return sum
