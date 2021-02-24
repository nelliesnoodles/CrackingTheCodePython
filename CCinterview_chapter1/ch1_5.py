#chapter 1 problem 5 

# NOTE:  There is a better, easier way to do this. 
# This could be cleaned up a lot. 
# this is not elegant.  Needs more tests.
    
   


def isReplace(str1, str2):
    # str2 is more than str1
    # the letters in str1 must be in str2
    one_pass = 0
    minstr = str2
    maxstr = str1
    max = len(str1) - 1
    check = len(str2) - 1
    if check > max:
        max = check
        maxstr = str2
        minstr = str1

    cycle = True
    i = 0
    j = 0
    val = True
    minmax = max - 1
    while cycle:

        #print('replace loop')
       
        if one_pass > 1:
            return False
            break
        if j > minmax:
            cycle = False
            break
        if i > max:
            cycle = False
            break
        
        #print('maxstr=', maxstr, 'max=', max)
        letter1 = maxstr[i]
        letter2 = minstr[j]
        
        if letter2 not in maxstr:
            return False
     
        if letter1 != letter2:
            i += 1            
            one_pass += 1
        else:
            i += 1
            j += 1
     
    return val

   
  

def isSwap(str1, str2):
    # They have the same amount of characters.
    # They can only have one each of a letter not in the other string.
    # example 'pbsk' 'kpba' => true
    # example 'pbbk' 'kpaa' => false 
    one_pass = 0
    max = len(str1) - 1
    cycle = True
    val = True
    i = 0
    while cycle:
        #print('swap loop')
        if one_pass > 1:
            cycle = False
            return False
       
        if i > max:
            cycle = False
            break

        letter1 = str1[i]
        letter2 = str2[i]
        if letter1 != letter2:
            one_pass += 1
        i += 1

    return val



def OneAway(str1, str2):
    diff = len(str1) - len(str2)
    absdiff = abs(diff)
    onediff = None

    if absdiff > 1:
        return False

    elif diff == 0:
        #print(f"swap: {str1} : {str2}")
        onediff = isSwap(str1, str2)
      

    elif diff == 1 or diff == -1:
        #print(f"replace: {str1} and/or {str2}.")
        onediff = isReplace(str1, str2)
    
    else:
        return 'Else clause Error'
   
    return onediff

def test1():
    # True:
    TEST1 = 'taste' #<= str1
    TEST2 = 'aste' #insert
    TEST3 = 'tast' #insert
    TEST4 = 'tastey'#remove 
    TEST5 = 'ttaste'#remove
    TEST6 = 'tastee'
    TEST7 = 'taxte'
    # False
    TEST8 = 'supercajafrajalisticexpealidocious' # <= str1
    TEST9 = 'upercajafrajalisticexpealidociou'
    TEST9 = 'supercajjaffrajalisticexpealidocious' 
    TEST10 = 'a'
    TEST11 = 'xx'
    TEST12 = 'supercajaffrajalisticexpealidociousx'
    TEST13 = 'sxpercajafrajalisticexpealidocioux'
    print('TEST TRUE----------')
    a = OneAway(TEST1, TEST2)
    b = OneAway(TEST1, TEST3)
    c = OneAway(TEST1, TEST4)
   
    d = OneAway(TEST1, TEST5)
    print(d)
    e = OneAway(TEST1, TEST6)
    f = OneAway(TEST1, TEST7)
    print(a, b, c, e, f)
    print('TEST FALSE----------')
    g = OneAway(TEST8, TEST9)
    h = OneAway(TEST8, TEST10)
    i = OneAway(TEST8, TEST11)
    j = OneAway(TEST8, TEST12)
    k = OneAway(TEST8, TEST13)
    print(g, h, i, j, k)
   
test1()





