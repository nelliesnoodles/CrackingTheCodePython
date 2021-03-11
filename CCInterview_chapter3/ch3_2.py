#chapter 3 problem 2

class StackNode(object):
    def __init__(self, data):
        self.next = None
        self.data = data
        # --- problem 2 
        self.minRef = None
        

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
        #--- problem 2
        self.min = None


    def push(self, data):
        node = StackNode(data)
        # -- problem 2, add self.min check
        if self.top == None:
            self.top = node
            self.size += 1
            self.min = node
        else:
            noderef = self.top
            node.next = self.top
            self.top = node
            self.size += 1
            if self.min.data > data:
                print('swapping min node:', node.data)
                node.minRef = self.min
                self.min = node
               
                
            else:
                node.minRef = self.min

    def get_min(self):
        #print("min = ", self.min)
        return self.min

    def pop(self):
        #remove top item
        # Can we get this to set a new min without going through the list to find the next minimum?
        # Even with the self.temp_min, if they pop this node off too, there's no reference to a third node
        # If the stack is 100's of items long, it would have to search each time.
        if self.top != None:

            if self.top == self.min:
                self.min = self.top.minRef

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


def test1():
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    numstack = Stack() 
    for num in nums:
        numstack.push(num)
    numstack.dump()
    for i in range(10):
        numstack.pop()
        print("Min:", numstack.get_min())
        
test1()