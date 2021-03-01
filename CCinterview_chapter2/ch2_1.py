from ch2_SetUp import Node, LinkedList
# The Node and LinkedList from ch2_SetUp are necessary unless you have your own LinkedList implementation to try it on.
# Being able to create your own Node and LinkedList is a great exercise, and I highly suggest it.
# chapter 2 problem 1

LL = LinkedList() 
duplicates = ['apple', 'orange', '56', 'Cloud', 'oranges', 'apple', 'apple', '56', 'Cloud Strife', 'Sephiroth']
for item in duplicates:
    LL.push(item)


def makeUnique(alinkedlist):
    alist = []
    start = alinkedlist.begin
    if start == None:
        return None 
    else:
        while start:
            data = start.data 
            if data in alist:
                alinkedlist.delete(data)
            else:
                alist.append(data)
            start = start.next
            


def test1():
    LL.printList()
    makeUnique(LL)
    print('*****  set:  ******')
    LL.printList() 

#test1()


# wihtout memory allocation
def Unique(alinkedlist):
    start = alinkedlist.begin
    if start == None:
        print('Empty!')
    else:
        while start:
            data = start.data
            print('data:', data)
           
            runner = start.next
            if runner != None:
                print('runner data:', runner.data)
            while runner:
                print('While runner:', runner)
                value = runner.data
                if data == value:
                    alinkedlist.delete(data)
                runner = runner.next
            start = start.next
            



LL2 = LinkedList() 
duplicates = ['apple', 'orange', '56', 'Cloud', 'oranges', 'apple', 'apple', '56', 'Cloud Strife', 'Sephiroth']
for item in duplicates:
    LL2.push(item)


def test2():
    #LL2.printList()
    Unique(LL2)
    print('*****  set:  ******')
    LL2.printList() 

#test2()