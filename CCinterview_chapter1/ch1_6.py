#chapter1 problem 6

def compress(astring, checkCapital=True):
    size = len(astring)

    count = 1
    highest_count = 2
   
    if not checkCapital:
        astring.lower()


    #cs = compressedstring
    cs = ''
    for i in range(0, size):
        current = astring[i]
        next = None
        #check if it's the last:
        if i == size - 1:
            cs += current + str(count)
            
        elif i + 1  < size:
            next = astring[i+1]
            if next == current:
                count += 1
               

            else:
                cs += current + str(count)
                count = 1
        else:
            print('else clause: for loop: compress(astring)')
   
    if len(cs) >= len(astring):
        return astring
    else:
        return cs
    

def test():
    TEST1 = 'aaabbbcdddeefffff'
    expected1 = 'a3b3c1d3e2f5'
    result1 = compress(TEST1)
    print(result1 == expected1)
    TEST2 = 'abbcdefghij'
    result2 = compress(TEST2)
    print(TEST2 == result2)
    TEST3 = 'AaaBbBcDeFffffGGGg'
    #wrong_result = 'A1a2B1b1B1c1D1e1F1f4G3g1'
    result = compress(TEST3, True)
    print(result == TEST3)
    TEST4 = compress(TEST3, True)
    print(TEST4 == TEST3)

test()


       


