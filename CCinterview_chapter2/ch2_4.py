from ch2_SetUp import Node, LinkedList

LL = LinkedList() 
values = [1, 2, 3, 
          7, 8, 9,
          1, 2, 3, 
          4, 5, 6
          ]

for item in values:
    LL.push(item)


def partition(val, alinkedlist):
   label = 'partition : ' + str(val)
   PNode = Node(label)
   head = None
   newbegin = None
   tail = None
   tailbegin = None
   
   node = alinkedlist.begin 
   while node:
       if node.data < val:
           if head == None:
               head = node
               newbegin = head
           else:
               head.next = node
               head = node
       if node.data >= val:
           if tail == None:
               tail = node 
               tailbegin = tail
           else:
               tail.next = node
               tail = node
       #print('node:', node)
       #print('head:', head)
       #print('tail:', tail)
       node = node.next

   if tail:
        tail.next = None
        PNode.next = tailbegin 
        alinkedlist.end =  tail
   else:
       PNode.next = None 
       alinkedlist.end = PNode 
   if head:
       head.next = PNode
       alinkedlist.begin = newbegin 

   else:
      PNode.next = tailbegin 
      alinkedlist.begin = PNode
   
    



       

def test1():
    # Change the value of where the partition is to test
    partition(3, LL)
    LL.printList()

test1()

   
               

               
               
                
            
            
    

    

