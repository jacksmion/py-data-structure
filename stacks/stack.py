#-*- coding:utf-8 -*-


class StackEmptyExcept(Exception):
    """
    栈空间为空
    """
    pass


class StackFullExcept(Exception):
    """
    栈空间满了
    """
    pass


class Stack:

    def __init__(self, size=-1):
        self._size = size
        self._list = list()

    def isEmpty(self):
        if 0 == len(self._list):
            return True

    def isFull(self):
        if self._size == -1:
            return False
        elif len(self._list) >= self._size:
            return True

    def pop(self):
        if self.isEmpty():
            raise StackEmptyExcept("Stack is Empty")
        else:
            self._list.pop()

    def push(self, data):
        if self.isFull():
            raise StackFullExcept("Stack is Full")
        else:
            self._list.append(data)

    def length(self):
        return len(self._list)

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return self._list.__str__()


# ---unittest------#
if __name__ == '__main__':
    s1 = Stack(10)
    [s1.push(i) for i in range(10)]
    print s1
    print s1.length()
