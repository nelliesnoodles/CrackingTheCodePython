#chapter 3 problem 1 
from ch3_SetUp import StackNode, Stack

class MultiStack():
    def __init__(self, numstacks, limit):
        self.numstacks = numstacks        
        self.stackarray = self._populate() 
        self.limit = limit 


    def _populate(self):
        newarray = []
        for i in range(self.numstacks):
            newstack = Stack() 
            newarray.append(newstack)
        return newarray

    def pop(self):
        #get top item in the top Stack within the array 
        topstack = self.stackarray[2]
        secondstack = self.stackarray[1]
        thirdstack = self.stackarray[0]
        if thirdstack.top == None:
            if secondstack.top == None:
                if topstack.top == None:
                    print("array is empty")
                    return None
                else:
                    return topstack.pop()                    
            else:
                return secondstack.pop()
        else:
            return thirdstack.pop()

    def push(self, data):
        topstack = self.stackarray[2]
        secondstack = self.stackarray[1]
        thirdstack = self.stackarray[0]

        if topstack.size <= self.limit:
            topstack.push(data)
        elif secondstack.size <= self.limit:
            secondstack.push(data)
        elif thirdstack.size <= self.limit:
            thirdstack.push(data)
        else:
            print("All stacks are full. Could not add new data.")
    
    def dump(self):
        for each in self.stackarray:
            each.dump() 


def test1():
    newMultistack = MultiStack(3, 10)
    for i in range(31):
        newMultistack.push(i)
    newMultistack.dump()

#test1()

def test2():
    newMultistack = MultiStack(3, 10)
    for i in range(31):
        newMultistack.push(i)
    newMultistack.dump()
    for i in range(31):
        print(newMultistack.pop())

test2()

