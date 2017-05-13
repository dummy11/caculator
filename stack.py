#!/user/bin/env python
# encoding: utf-8

"""
@Version: python2.7
@Author: 'linyue.li'
@License: personality reserved
@Site: 'www.dummy11.com'
@File_name: .py
@Time : 2017/05/05 15:20
@Discription: ...
"""

class PyStack(object):

    def __init__(self,contents = None, size = 10):
        self.items = [None]*size
        self.item_len = 0
        self.item_index = 0
        self.maxsize = size
        ## stack head pointer
        self.top = -1

        for self.item_index in range(len(contents)):
            self.top += 1
            self.items[self.item_index] = contents[self.item_index]


    def push(self,data):
        if self.top != self.maxsize - 1 :
            self.top += 1
            self.items[self.item_index] = data
        else:
            raise IndexError('The stack is full')

    def pop(self):
        if self.top != - 1:
            item =  self.items[self.top]
            self.top -= 1
            return item
        else:
            raise IndexError('The stack is empty')

    def getsize(self):
        return len(self.items)

    def tranverse(self):
        while self.top != -1 :
            item =  self.items[self.top]
            print item
            self.top -= 1



def main():
    """test routine for the file"""
    stack0 = PyStack([1,2,3,4,5])
    print stack0.getsize()
    stack0.tranverse()
    print stack0.getsize()


if __name__ == '__main__':
    main()
