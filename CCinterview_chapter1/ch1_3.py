#chapter 1 problem 3
# I'm going to exclude description, as I don't know if that falls in the realm of plagirism.
# In Java and Python strings are immutable.  Meaning we can not change the original string, only assign/return a new value;
def replace(acharorset, bstring, newvalue):
    newstring = ''
    for char in bstring:
        if char == acharorset:
            newstring += newvalue
        else:
            newstring += char

    return newstring


def test1():
    startstring = 'A waffle House.'
    endstring = 'A%20waffle%20House.'
    result = replace(' ', startstring, '%20')
    if result != endstring:
        print('Fail.')
    else:
        print('Pass')

def main():
    print("***************")
    print("Start Test")
    test1() 
    print("***************")

main()




