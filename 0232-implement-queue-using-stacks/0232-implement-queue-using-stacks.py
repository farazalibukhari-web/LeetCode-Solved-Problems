from collections import deque

class MyQueue(object):

    def __init__(self):
        self.arr = deque()

    def push(self, x):
        self.arr.append(x)   # enqueue to the right

    def pop(self):
        if not self.empty():
            return self.arr.popleft()  # dequeue from the left

    def peek(self):
        if not self.empty():
            return self.arr[0]

    def empty(self):
        return len(self.arr) == 0
