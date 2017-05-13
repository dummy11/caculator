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


class PyLinkedStack(object):
    def __init__(self):
        """first is the stack head pointer
        """
        self.first = PyLinkedStack.__Node(None, None)
        self.last = self.first
        # -1 means the stack is empty
        self.num_node = -1

    class __Node(object):
        def __init__(self, item=None, next_node = None):
            self.item = item
            self.next = next_node

    def push(self, data):
        node = PyLinkedStack.__Node(data, None)
        node.next = self.first
        self.first = node
        self.num_node += 1


    def pop(self):
        if self.num_node != -1:
            item = self.first.item
            self.first = self.first.next
            self.num_node -= 1
            return item
        else:
            raise IndexError('the stack is empty')

def main():
    """test routine for the file"""
    stack0 = PyLinkedStack()
    stack0.push(1)
    stack0.push(2)
    stack0.push(3)
    print stack0.pop()
    print stack0.pop()
    print stack0.pop()


if __name__ == '__main__':
    main()
