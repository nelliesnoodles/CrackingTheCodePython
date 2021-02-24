# Chapter 1 problem 2 

"""
Given two strings, write a method to decide if one is a permutation of the other.
"""

# with data operators

def isSame(s1, s2):
    sl1 = list(s1)
    sl2 = list(s2)
    #print(sl1, sl2)
    if len(sl1) != len(sl2):
        return False
    else:
       sl1_sorted = sorted(sl1)
       
       sl2_sorted = sorted(sl2)
       max = len(sl2_sorted) 
       for i in range(0, max):
           char1 = sl1_sorted[i]
           char2 = sl2_sorted[i]
           if char1 != char2:
               return False
    return True
           

def test1():
    astring = 'hhyutiopp'
    bstring = 'yupptihoh'
    result = isSame(astring, bstring)
    return result

def test2():
    astring = 'hhyut&iopp'
    bstring = 'y$upptihoh'
    result = isSame(astring, bstring)
    return result

def main():
    print('************')
    print('Start Test')
    if test1() != True:
        print('Fail')
    else:
        print('Pass')
    if test2() != False:
        print('Fail')
    else:
        print('Pass')

main()

