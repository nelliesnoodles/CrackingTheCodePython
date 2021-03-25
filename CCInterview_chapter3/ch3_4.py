#chapter 3 problem 4
from ch3_SetUp import StackNode, Stack 


class MyQueue(object):
    def __init__(self):
       
        self.start = Stack()
        self.end = Stack()

    def push(self, data):
        #push data so that first in is first out from the stacks 
        self.start.push(data)

    def reverseStack(self):
        node = self.start.top 
        while node:
            data = node.data
            self.end.push(data)
            node = node.next

    def create_Queue(self):
        self.end = Stack() 
        self.reverseStack() 

    def dump_queue(self):
        node = self.end.top
        while node:
            print(node)
            node = node.next

    def dump_stack(self):
        node = self.start.top
        while node:
            print(node)
            node = node.next 


def test1():
    myqueue = MyQueue() 
    for i in range(20):
        myqueue.push(i)
    myqueue.create_Queue()
    print("---", "QUEUE, first in first out ---")
    myqueue.dump_queue()
    print("---", "STACK, first in last out ---")
    myqueue.dump_stack()


test1()


