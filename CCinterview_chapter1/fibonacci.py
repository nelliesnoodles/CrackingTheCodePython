#!/user/bin/Python3

#  fibonacci and recursion
CACHE = [1, 1, 2, 3, 5]


#brute force

def fibof(n):
    if n <= 1:
        return 1 
    elif n == 2:
        return 2 
    elif n == 3:
        return 3
    else:
        start = 2
        current = 3
        for i in range(1, n - 3):
            print(start, current)
            temp = current
            
            current = start + current

            start = temp 
        return current 

def test1():
     N = 8
     print(fibof(N))
            

#test1()

# use cache

def fibof2(n):
    
    length = len(CACHE)
    last = length - 1
    #print(n, length)
    
    if n < length:
        num = CACHE[n]
        print('Returning Cache')
        return num
    else:
        previous = CACHE[-2]
        current = CACHE[-1]
       
        for i in range(last, n - 1):
            
            temp = current            
            current = previous + current
            CACHE.append(current)
            previous = temp 
           
           

        return current 
    


def test2(N):
    
     print(fibof2(N))
            


#test2(7)

def testmany():
    for i in range(7, 21):
        fibof2(i)
    #print('USING CACHE')
    fibof2(19)

#testmany()

# With recursion

def fibrecur(N):
    if N <= 1:
        return N
    else:
        return (fibrecur(N-1) + fibrecur(N-2))

    
def test4():
    n = 13 
    num = fibrecur(n)
    print(num)

test4()



