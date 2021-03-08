#chapter 2 problem 6
from ch2_SetUp import Node, LinkedList 

notPali1 = "abbcbbac" #even
notPali2 = "acccb" #odd
Pali1 = "abbbba" #odd
Pali2 = "aabbaa" #even 

LLnot1 = LinkedList() 
LLnot2 = LinkedList()
LLisPali1 = LinkedList()
LLisPali2 = LinkedList() 

for char in notPali1:
    LLnot1.push(char)
for char2 in notPali2:
    LLnot2.push(char2)
for char3 in Pali1:
    LLisPali1.push(char3)
for char4 in Pali2:
    LLisPali2.push(char4)

def isPalindrome(linkedlist):
    forwardstring = ''
    backwardstring = ''
    node = linkedlist.begin 
    while node:
        data = str(node.data)
        forwardstring += data 
        backwardstring = data + backwardstring
        node = node.next

    if forwardstring == backwardstring:
        return True 
    else:
        return False 

def test1():
    #isPalindrome(linkedlist)
    print("Should be:  True")
    #LLisPali1 = LinkedList()
    #LLisPali2 = LinkedList() 
    testtrue1 = isPalindrome(LLisPali1)
    testtrue2 = isPalindrome(LLisPali2)
    print("testtrue1:", testtrue1)
    print("testtrue2:", testtrue2)
    print("\n Should be: False")
    #LLnot1 = LinkedList() 
    #LLnot2 = LinkedList()
    testfalse1 = isPalindrome(LLnot1)
    testfalse2 = isPalindrome(LLnot2)
    print("testfalse1:", testfalse1)
    print("testfalse2:", testfalse2)
    print("END TESTs")


test1()