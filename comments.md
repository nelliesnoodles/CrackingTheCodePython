# Comments:

### 2-24-2021
A commit of the file [ch1_5.py] had a commit comment of _not recommended_.  
This commit message was inteded to reference the code in the file, and in no way the book or it's problems/solutions.
-NT


### chapter 1 problem 6 :  2-25-2021
() example::  'astring' + 'bstring' = "astringbstring"
Because of Python's ability to 'build strings' I don't think the Java Stringbuilder method is necessary to deplete the complexity of the solution.
I could totally be wrong.
-NT

### chapter 1 problem 7 : 2-25-2021
The code does not include an 'inplace' transformation
-NT

### chapter1 problem 9 : 2-26-2021
The author uses 'rotation' and 'permutation' in the problem description.
Because I wanted to try before I looked at the solution, there is an extra method/function in the file that finds if a string is a permutation of the first one. 
It's the same string, just scrambled.  

The solution did not want this resolution, but I left it in for prosterity. 

### chapter 2 3-1-2021
Because there are many differences in the way C implements memory allocation, Just keep in mind that with Python a whole lot of work is done under the hood 
that we will never have to worry about.   

_Example:  Garbage Collection_

Explanation:  [basics of memory management in python](https://stackabuse.com/basics-of-memory-management-in-python/)

### chapter 2 3-4-2021
The ch2_SetUp.py had some changes. There are links in the Notes to explain what I had to change.  When using the 'or None' in the __ repr__ function of Node(), a zero was seen as falsy, and then the data variable printed was sent as 'None'.  

