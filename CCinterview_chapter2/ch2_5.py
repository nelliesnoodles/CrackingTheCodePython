# chapter 2 problem 5
from ch2_SetUp import Node, LinkedList 

nums = [1, 3, 4]
nums2 = [0, 0, 6]
nums3 = [1, 0, 8, 9, 9]
LL=LinkedList()
LL2=LinkedList()
LL3=LinkedList()

for num in nums:
    LL.push(num)
for num2 in nums2:
    LL2.push(num2)
for num3 in nums3:
    LL3.push(num3)


def sumTwo(ll1, ll2, reverse=True):
    sum = 0  
    node1 = ll1.begin 
    node2 = ll2.begin
    num1 = 0 
    num2 = 0
    tens = 10 
    count = 0
    total = 0
    newLL = LinkedList()

    # What if one linked list is bigger than another? Do we assume they are the same size?
    
    if reverse:
        
        while node1:
            current = node1.data
       
     
            if current != 0 and current != '0':
                num = node1.data * tens**count
                total = num + total 
            count += 1
            node1 = node1.next

        count = 0 

        while node2:
            current = node2.data
       
        
            if current != 0 and current != '0':
                num = node2.data * tens**count 
                total = num + total 
            count += 1 
            node2 = node2.next
        numstring = str(total)

        for char in numstring:
            # note:  Is this the cheating she refers to?
            data = int(char)
            newLL.push(data)
        

        

    else:
        print('reverse=false')
        adding = True
        carry = 0
        
        while adding:
            data1 = None 
            data2 = None
            
            if node1:
                data1 = node1.data
                node1 = node1.next 
            
            if node2: 
                data2 = node2.data
                node2 = node2.next
            #print('carry:', carry)
            #print('data1:', data1)
            #print('data2:', data2)
            if data1 == None and data2 == None:
                break
            elif data1 != None and data2 != None:
                total = data1 + data2 + carry

            elif data1 == None:
                total = data2 + carry
               
            elif data2 == None:
                total = data1 + carry  
               
            else:
                print("ERROR: This should not happen.")
                break

            if total >= 10:
                carry = 1
                sumof = total - 10 
                newLL.push(sumof)
            else:
                carry = 0
                newLL.push(total)
           
            if node1 == None and node2 == None and carry > 0:
                newLL.push(carry)



    return newLL

def test1():
    total = sumTwo(LL, LL2)
    total.printList()

#test1()

def test2():
    total = sumTwo(LL, LL2, False)
    total.printList()

#test2()

def testwonky():
    total = sumTwo(LL3, LL, False)
    total.printList()

testwonky()
