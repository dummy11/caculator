#!/user/bin/env python
# encoding: utf-8

"""
@Version: python2.7
@Author: 'linyue.li'
@License: personality reserved
@Site: 'www.dummy11.cm'
@File_name: .py
@Time : 2017/05/05 15:20
@Discription: ...
"""

# import lxml


class PyLinkedList(object):
    """the class is a linked construct list"""


    class __Node(object):
        def __init__(self, item = None, next = None):
            self.item = item
            self.next = next

        def setitem(self,item):
            self.item = item

        def getitem(self, item):
            return self.item

        def getnext(self):
            return self.next

        def setnext(self,next):
            self.next = next

    def __init__(self,):
        self.first = PyLinkedList.__Node(None, None)
        self.last = self.first
        self.num_items = 0

    def append(self,item):
        node = PyLinkedList.__Node(item, None)

        self.last.setnext(node)
        self.last = node
        self.num_items += 1

    def insert(self,index,item):
        cursor = self.first
        if(index < self.num_items):
            for i in range(index):
                cursor = cursor.getnext()

            node = PyLinkedList.__Node(item, cursor.getnext())
            cursor.setnext(node)
            self.num_items += 1
        else:
            self.append(item)

    def delete(self,index):
        cursor = self.first
        if(index < self.num_items):
            for i in range(index-1):
                cursor = cursor.getnext()

            node = cursor
            cursor = cursor.getnext()
            cursor = cursor.getnext()
            node.setnext(cursor)
        else:
            raise IndexError('the index is out of range')



    ##def __setitem__(self, key, value):



    ##def __getitem__(self, item):




def main():
    """test routine for the file"""

if __name__ == '__main__':
    main()

