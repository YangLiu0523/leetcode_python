# Copyright: Internal Use Only
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2019-02-23 16:43:50


class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def empty(self):
        return len(self.data) == 0

    def top(self):
        return self.data[-1]


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = Stack()
        while not self.data.empty():
            tmp.push(self.data.pop())

        val = tmp.pop()

        while not tmp.empty():
            self.data.push(tmp.pop())
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp = Stack()
        while not self.data.empty():
            tmp.push(self.data.pop())

        val = tmp.top()

        while not tmp.empty():
            self.data.push(tmp.pop())
        return val


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.data.empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
