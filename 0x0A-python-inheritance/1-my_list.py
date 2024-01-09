#!/usr/bin/python3
# saadsgh123 <sdsghouri@gmail.com>
# 1-my_list.py
class MyList(list):

    def append(self, __object):
        super().append(__object)

    def print_sorted(self):
        print(sorted(self))


if __name__ == '__main__':
    # my_list = MyList([1, 3, 2])
    my_list = list([1, "saad"])
    # my_list.print_sorted()
    # print(my_list)
