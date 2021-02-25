#chapter 1 problem 7

"""  CONTEXT ASCII:
     pixel = [ ]
     content of pixel = [ some INT ]
     MATRIX:
     [a] [0] [0] [0] [0] [0] [0] [0] [0] [x]
     [1] [1] [1] [1] [1] [1] [1] [1] [1] [1]
     [2] [2] [2] [2] [2] [2] [2] [2] [2] [2]
     [3] [3] [3] [3] [3] [3] [3] [3] [3] [3]
     [4] [4] [4] [4] [4] [4] [4] [4] [4] [4]
     [5] [5] [5] [5] [5] [5] [5] [5] [5] [5]
     [6] [6] [6] [6] [6] [6] [6] [6] [6] [6]
     [7] [7] [7] [7] [7] [7] [7] [7] [7] [7]
     [8] [8] [8] [8] [8] [8] [8] [8] [8] [8]
     [y] [9] [9] [9] [9] [9] [9] [9] [9] [b]

     ROTATED 90 degrees:
     [y] [8] [7] [6] [5] [4] [3] [2] [1] [a]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [9] [8] [7] [6] [5] [4] [3] [2] [1] [0]
     [b] [8] [7] [6] [5] [4] [3] [2] [1] [x]




      column contents = row[i]
     python matrix: [
     [...[]*10], <== row
         [...[]*10],
          [...[]*10],
           [...[]*10],
            [...[]*10],
             [...[]*10],
              [...[]*10],
               [...[]*10],
                [...[]*10],
                 [...[]*10],
       ]
"""

def rotate(amatrix):
    # Matrix is N by N
    size = len(amatrix)
    #By adding width and hieght, we can rotate a N by M matrix
    #Since we know we want it 90 degrees, this is the only change to make N*M possible. 
    #If it were 270 degrees, this bit would still be ok, but all the cells would need to be in a different order
    width = len(amatrix[0])
    height = len(amatrix)
    indexes = size - 1
    newmatrix = []
    if len(amatrix) == 0:
        return amatrix

   
    for i in range(0, width):
        newmatrix.append([])    
    # Each item in a row now becomes the column from end => start
    # reverse the for loop
    for row in amatrix:
        #[a][0][0][...][x]
        i = 0
            
        for cell in row:
                #[a]                
            newmatrix[i].append(cell)
            #print(newmatrix[i])
            i+= 1
            #print(cell)
        i = 0

    for i in range(0, size):
        
        current = newmatrix[i]
        #reverse the list
        x = reversed(current)
        # reversed returns an iterator object, convert to list
        x = list(x)
        newmatrix[i] = x

    return newmatrix



def createNNMatrix(n):
    matrix = []
    for i in range(0, n + 1):
        row = []
        for k in range(0, n + 1):
            #data = 'R:' + str(i) + 'C:' + str(k)
            #data = i*100 + k
            data = str(i) + ':' + str(k)
            row.append([data])
        matrix.append(row)
    return matrix


def test():
    matrix = [
        [['0-one'], ['0-two'], ['0-three']],
        [['1-one'], ['1-two'], ['1-three']],
        [['2-one'], ['2-two'], ['2-three']]
        ]
    for item in matrix:
        print(item)
    result = rotate(matrix)
    for item2 in result:
        print(item2)

    # fail- Can not rotate N*M with this rotate()
    matrix2 = [
        [[101], [102], [103], [104]],
        [[201], [202], [203], [204]],
        [[301], [302], [303], [304]],        
        ]
    print(rotate(matrix2))
    # To see the larger matrixes, in windows powershell you can right click the menu bar for options,
    # and shrink the text size.  But it gets really hard to see.
    #matrix3 = createNNMatrix(15)
    #result2 = rotate(matrix3)
    #for item3 in result2:
        #print(item3)
    

test()
            


                



