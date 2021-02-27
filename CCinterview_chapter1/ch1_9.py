#chapter 1 problem 9
#
#Reference link: https://www.geeksforgeeks.org/string-slicing-python-rotate-string/

#Reference Code:
 
def rotate(input,d):  
  
    # slice string in two parts for left and right  
    Lfirst = input[0 : d]  
    Lsecond = input[d :]  
    Rfirst = input[0 : len(input)-d]  
    Rsecond = input[len(input)-d : ]  
  
    # now concatenate two parts together  
    print ("Left Rotation : ", (Lsecond + Lfirst) ) 
    print ("Right Rotation : ", (Rsecond + Rfirst))  




# NOT A SOLUTION FOR ROTATION.
# only finds if it's matching string contents.
def isSubstring(s1, s2):
    # Uses test1()
    # Globals STRING1 => STRING6
    # Not correct solution, but maybe useful?
    temp1 = list(s1)
    temp2 = list(s2)
    if len(s1) != len(s2):
        return False
    for i in range(0, len(s2)):
        letter = s2[i]
        if letter in temp1 and letter in temp2:
           temp1.remove(letter)
           temp2.remove(letter)
        else:
            return False
    if len(temp1) == 0 and len(temp2)==0:
        return True
    else:
        return False

#  TRUE
STRING1 = 'ThisIsASubstring'
STRING2 = 'IsASubstringThis'
#  FALSE
STRING3 = "watacosarethebest"
STRING4 = "wafflesarethebest"
# TRUE 
STRING5 = 'Tim,IsAbeautifulMan'
STRING6 = 'Man,IsTimbeaAutiful'

def test():
    # Not for solution. 
    # Finds strings that are permutations
    # Matching characters in a different order
    print(isSubstring(STRING1, STRING2))
    print(isSubstring(STRING3, STRING4))
    print(isSubstring(STRING5, STRING6))


def doesContain(s1modified, s2):
    if s2 in s1modified:
        return True
    else:
        return False

def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) <= 0 or len(s2) < 0:
        return False

    modified = s1 + s1
    return doesContain(modified, s2)

def test2():
    STRINGs1 = 'tacocat'
    STRINGs2 = 'cattaco'
    print('TRUE:', isRotation(STRINGs1, STRINGs2))
    STRINGs3 = 'ArealNiceShrubbery'
    STRINGs4 = 'NiceArealShrubbery'
    print('FALSE:', isRotation(STRINGs3, STRINGs4))
    STRINGs5 = 'delicatepaperdolls'
    STRINGs6 = 'paperdollsdelicate'
    print('TRUE:', isRotation(STRINGs5, STRINGs6))

test2()


