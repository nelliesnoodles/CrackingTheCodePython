#chapter 2 problem 8

from ch2_SetUp import Node, LinkedList


# CAUTION:
# using printList() *while loop* on a linkedlist with a loop, will cause an infinite loop of printing.
LLisLoop = LinkedList()
loopNode = Node("LOOP")
for i in range(20):
    if i == 10:
        LLisLoop.pushNode(loopNode)
    else:
        LLisLoop.push(i)

#set the loop
LLisLoop.end.next = loopNode 
 
def findLoop(linkedlist):
    node1 = linkedlist.begin
    count = 0
    if node1 == None:
        print("This linked list is empty")
        return None
    
    runner = linkedlist.begin.next

    if runner:
        while node1 and runner:
            if node1 == runner:
                print("loop node found.")
                print("count=", count)
                return runner
            if runner.next:
                if runner.next == node1:
                    print("loop node found.")
                    print("count=", count)
                    return node1 
                if runner.next == node1.next:
                    print("loop node found.")
                    print("count=", count)
                    return runner.next
                runner = runner.next
            node1 = node1.next
            runner = runner.next 
            count += 1
    else:
        "This linked list has only one item."
        return None


def test1():
    #LLisLoop = LinkedList()
    #loopNode = Node("LOOP")
    #findLoop(linkedlist)
    result = findLoop(LLisLoop)
    #count = 9
    print(result)

#test1()

def test2():
    #worst case: Loop node is at the end, pointing at the first node.
    LLisLoop2 = LinkedList()
    loopNode2 = Node("LOOP2")
   
    for i in range(20):
         if i == 19:
             LLisLoop2.pushNode(loopNode2)
         else:
             LLisLoop2.push(i)

    #set the loop
    begin = LLisLoop2.begin
    loopNode2.next = begin

    result = findLoop(LLisLoop2)
    #count = 18
    print(result)

test2()

            




