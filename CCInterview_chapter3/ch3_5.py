#chapter 3 problem 5
from ch3_SetUp import StackNode, Stack
from random import randint


# refernce link: https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/
def sortStack(stack):
   
    newStack = Stack() 
   
    while(not stack.isEmpty()):
        # remove the last item place it in tmp
        tmp = stack.pop() 
        less_than = True #greatear_than if you flip the gator jaws
        while(not newStack.isEmpty() and less_than):
            x = newStack.peek()
            if x < tmp: # flipping the gator jaws will sort the list in the reverse order.
                lesser = newStack.pop()
                stack.push(lesser)
            else:
                #stop here, the next value is greater_than the tmp value
                #we want the tmp value pushed to the newStack at this point
                less_than = False
        # The values that were pushed back into the stack are in order in comparison to the newly appended tmp.  
        # The outer loop will quickly loop through and append them to the newStack, as they are, in order, less_than the next popped() value
        # Once it gets to the tmp value that is greater than the last item in the newStack, it will remove all of them again,
        # pushing them onto the original stack, in order, and then appending the larger tmp value to our newStack, and the process loops. 
        newStack.push(tmp)    

    return newStack

#test one was not useful in any way, and may have been what was blocking my progress.


def test2():
    astack = Stack() 
    for i in range(10):
        ranX = randint(0, 100)
        astack.push(ranX)
    #astack.dump()
    newstack = sortStack(astack)
    newstack.dump()
    print(newstack.top)

test2()



 

  

 
   



            




            
   
