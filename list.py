#!/user/bin/env python
# encoding: utf-8

"""
@Version: python2.7
@Author: 'linyue.li'
@License: personality reserved
@Site: 'www.dummy11.com'
@File_name: .py
@Time : 2017/4/28 15:20
@Discription: ...
"""


class PyList(object):
    def __init__(self, contents=None, size=10):
        """default value of function arguments should not be mutable"""
        # if contents is None:
        self.items = [None] * size
        self.items_len = 0
        self.size = size
        self.item_index = 0

        # added contets to the end of the list
        # for item in contents:
        for self.item_index in range(len(contents)):
            # self.items.append(item)
            self.items[self.item_index] = contents[self.item_index]
        print (self.items)

    def __getitem__(self, index=1):
        """index is the position of the list"""
        if index < 1 or index > self.size:
            raise IndexError('the index is out of range')

        return self.items[index-1]

    def __setitem__(self, key, value):
        """key is the position of the list"""
        if key < 1 or key > self.size:
            raise IndexError('the index is out of range')
        self.items[key-1] = value

    def __makeroom(self):
        self.items_new = [None]*(self.size+1)
        self.size += 1
        for index in range(len(self.items)):
            self.items_new[index] = self.items[index]

        self.items = self.items_new

    def append(self, value):
        self.__makeroom()
        self.items[self.size-1] = value

    def __str__(self):
        s = None
        for index in range(len(self.items)):
            s = "["
            print self.items[index],
            s += repr(self.items[index])
            s += "]"

        return s

    def insert(self,index,item):
        pass

    def delete(self,index):
        pass


def main():
    # a space is requres after ',',
    # list0 = PyList(['hello', 'world'])
    list0 = PyList(['1', 2])
    # item = list0.__getitem__(11)
    item = list0[10]
    print(item)

    list0[10] = 5
    item = list0[10]
    print(item)

    list0.append(8)

    str(list0)


if __name__ == '__main__':
    main()
