#chapter 1 problem 4

#'XAXXAX' => 'XXXXAA'
#'XXXAAA' => 'XAXAX / A'
STRING1 = 'appleelppa' # true
STRING2 = 'abababc' # false
STRING3 = 'aaaabbbby' # true
STRING4 = 'aaaa78bbbb' # false 

# Clarification:  Casing of characters && spacing. 
# With this solution, Capitalized A, and a, are not the same Character. 

# Live with Noah Gibbs: https://www.youtube.com/watch?v=KQ9nz9SEfA4
# reference:
# link: https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes

def allChars(astr, char):
    alist = []
    for letter in astr:
        if letter == char:
            alist.append('X')
    return alist
        


def isPalindrome(astring):
    even = False
    evenchars = 0
    oddchars = 0
    astrSet = set(astring)
    count_odd = 0
    if len(astring) % 2 == 0:
        even = True
        
    
    for letter in astrSet:
        indexes = allChars(astring, letter)
        #print(letter, indexes)
        if len(indexes) % 2 != 0:
            #print(astring, letter, indexes)
            count_odd += 1

    if even:
        #print('even:', count_odd)
        if count_odd > 0:
            return False
        else:
            return True
    if not even:
        #print('odd:', count_odd)
        if count_odd != 1:
            return False
        else:
            return True
    

def test1():
    result1 = isPalindrome(STRING1)
    result2 = isPalindrome(STRING2)
    result3 = isPalindrome(STRING3)
    result4 = isPalindrome(STRING4)
    if result1 != True:
        return 'Fail'
    if result2 != False:
        return 'Fail'
    if result3 != True:
        return 'Fail'
    if result4 != False:
        return 'Fail'
    return 'Pass'
   

def main():
    print("**    START TEST   **")
    print(test1())
    print("**     END TEST    **")

main()