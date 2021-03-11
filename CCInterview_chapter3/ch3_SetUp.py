#Chapter 3 Set Up
#References:
   #link:(deque-stack import) https://www.geeksforgeeks.org/stack-in-python/



class StackNode(object):
    def __init__(self, data):
        self.next = None
        self.data = data
        

    def __repr__(self):
        data = self.data #<=  Changed  data = self.data or None was setting 0 as None.
        # reference Link: https://stackoverflow.com/questions/8747740/assignment-with-or-in-python
       
        data = str(data)
        # Removed ' or None'  to account for data that is the zero integer
        if self.next != None:
            next = self.next and self.next.data
        else:
            next = 'None'
        dataString = f"[ data: {data}, next: {next} ]"
        return dataString

class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data):
        node = StackNode(data)
        if self.top == None:
            self.top = node
            self.size += 1
        else:
            node.next = self.top
            self.top = node
            self.size += 1
    def pop(self):
        #remove top item
        if self.top != None:
            item = self.top.data 
            new = self.top.next 
            self.top = new 
            self.size -= 1 
            return item 
        else:
            #raise ValueError 
            print("Can not pop() from empty stack.")
            return None

    def peek(self):
        if self.top != None:
            return self.top.data 
        else:
            print("Empty stack.")
            return None 
    def isEmpty(self):
        return self.top == None

    def dump(self):
        print("Start stack:")
        if self.top != None:
            temp = self.top
            while temp:
                print(temp)
                temp = temp.next
        else:
            print("EMPTY")
        print(":End stack")




class QueueNode(object):
    def __init__(self, data):
        self.next = None
        self.data = data
        

    def __repr__(self):
        data = self.data #<=  Changed  data = self.data or None was setting 0 as None.
        # reference Link: https://stackoverflow.com/questions/8747740/assignment-with-or-in-python
       
        data = str(data)
        # Removed ' or None'  to account for data that is the zero integer
        if self.next != None:
            next = self.next and self.next.data
        else:
            next = 'None'
        dataString = f"[ data: {data}, next: {next} ]"
        return dataString


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, data):
        node = QueueNode(data)
        if self.first == None:
            self.first = node 

        elif self.first != None and self.last == None:
            self.first.next = node 
            self.last = node 
        else:
            self.last.next = node 
            self.last = node 
        self.size += 1

    def remove(self):
        if self.first != None:
            item = self.first.data 
            self.first = self.first.next
            self.size -= 1
            if self.first == self.last:
                self.last = None 
            return item
        else:
            print("Can not remove() from empty Queue.")
            return None

    def peek(self):
        if self.first != None:
            return self.first.data 
        else:
            print("Empty Queue.")
            return None
    def isEmpty(self):
        return self.first == None and self.last == None

    def dump(self):
        print("Start Queue:")
        temp = self.first
        if temp != None:
            while temp:
                print(temp)
                temp = temp.next 
        else:
            print("EMPTY")
        print(":End Queue")

    

def testStack():
    newStack = Stack() 
    for i in range(10):
        newStack.push(i)
    newStack.dump() 
    for j in range(10):
        x = newStack.pop()
        print(x)
    print("newstack is Empty:", newStack.isEmpty())


#testStack()

def testQueue():
    newQueue = Queue()
    for n in range(10):
        newQueue.add(n)
    newQueue.dump() 
    for m in range(10):
        x = newQueue.remove()
        print(x)
    print("Queue is empty = ", newQueue.isEmpty())


testQueue()





