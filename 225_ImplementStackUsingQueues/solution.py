# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-22 23:52:13


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        return self.data.pop(0)

    def empty(self):
        return len(self.data) == 0

    def top(self):
        return self.data[0]


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()


    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        self.q2.enqueue(x)
        while not self.q1.empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.dequeue()

    def top(self) -> 'int':
        """
        Get the top element.
        """
        return self.q1.top()

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
