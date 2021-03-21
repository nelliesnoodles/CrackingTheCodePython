#chapter 3 problem 3

from ch3_SetUp import StackNode, Stack


class SetOfStacks(object):
    def __init__(self):
        self.stack = [Stack()]
        self.max = 10
        self.currentStack = 0
        
    def push(self, data):
        current = self.stack[self.currentStack]
        length = current.size
        if length < self.max:
            current.push(data)
        else:
            newStack = Stack() 
            newStack.push(data)
            self.stack.append(newStack)
            self.currentStack += 1 

    def pop(self):
        current = self.stack[self.currentStack]
        #print(current)
        if current.size == 0:
            return None
        else:

            if current.size > 1:
                return current.pop()
            else:
                item = current.pop() 
                if self.currentStack != 0:
                    self.stack.pop() 
                    self.currentStack -= 1 
                return item 


    def popAt(self, ind):
        if self.stack[0].size == 0:
            return None
        elif len(self.stack) - 1 < ind:
            raise IndexError
        else: 
            asset = self.stack[ind]
            item = asset.pop() 
            if asset.size <= 0 and ind != 0:
                del self.stack[ind]
                self.currentStack -= 1 
            return item


    def dump(self):
        count = 0
        for stack in self.stack:
            print("*-*" * 5)
            print('stack number =', count)
            stack.dump()
            count += 1




def test1():
    plates = SetOfStacks() 
    for i in range(50):
        plates.push(i)
    plates.dump()

#test1()

def test2():
    plates = SetOfStacks() 
    for i in range(50):
        plates.push(i)
    for i in range(10):
        x = plates.pop()
        print("popped:", x)
    plates.dump()

#test2()

def test3():
    plates = SetOfStacks() 
    for i in range(50):
        plates.push(i)
    for i in range(50):
        plates.pop()
    plates.dump()


#test3()

def test4():
    plates = SetOfStacks() 
    for i in range(50):
        plates.push(i)
    # 0 = 9, 1 = 19, 2 = 29, 3 = 39, 4 = 49 
    print(plates.popAt(0))
    print(plates.popAt(1))
    print(plates.popAt(2))
    print(plates.popAt(3))
    print(plates.popAt(4))
    plates.dump()

#test4()







        








        
        



