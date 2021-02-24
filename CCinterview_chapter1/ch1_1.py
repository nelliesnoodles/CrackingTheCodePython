#chapter 1, question 1 
# implement an algorithm to determine if a string has all unique characters.

# with additional data space:

def unique(astring):
    liststring = list(astring)
    setstring = set(astring)
    if len(liststring) == len(setstring):
        return True
    return False


def test1():
    notunique = 'abcdeffghijklmopqrst789-@#$'
    isUnique = 'asdfghjkl!@#$%^&*()'
    testpass = "Pass"
    if unique(notunique) == True:
        return "Fail"
    if unique(isUnique) == False:
        return "Fail"
    return testpass


# Without additional data 

#reference solution:
#link: https://www.geeksforgeeks.org/efficiently-check-string-duplicates-without-using-additional-data-structure/
# Returns true if all characters of str are  
# unique.  
# Assumptions : (1) str contains only characters  
#                    from 'a' to 'z'  
#                (2) integers are stored using 32  
#                    bits 
  
def areCharactersUnique(s): 
      
    # An integer to store presence/absence  
    # of 26 characters using its 32 bits 
    checker = 0
      
    for i in range(len(s)): 
          
        val = ord(s[i]) - ord('a') 
          
        # If bit corresponding to current  
        # character is already set 
        if (checker & (1 << val)) > 0: 
            return False
          
        # set bit in checker  
        checker |= (1 << val) 
          
    return True  
  

# How does bitwise work??


#without bitwise:
def unique2(s):
    #s is string   
   for character in s:
       #print('**************')
       #print(s.find(character))
       #print(s.rfind(character))
       #print('**************')
       x = s.find(character)
       y = s.rfind(character)
       if x != y:
           return False
   return True

def test2():
    
    notunique = 'abcdeffghijklmopqrst789-@#$'
    isUnique = 'asdfghjkl!@#$%^&*()'

    if unique2(notunique) != False:
        return 'Fail.'
    if unique2(isUnique) != True:
        return 'Fail.'
    return 'Pass.'





def main():
    print("start tests ....")

    print(test1())
    print(test2())

    print("end tests ....")

    # run reference code:
    teststring = 'aza'
    areCharactersUnique(teststring)

#main()
