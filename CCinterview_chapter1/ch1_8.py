#chapter 1 problem 8


TESTMATRIX5x7 = [
    [[0],[1],[1],[1],[0],[1],[1]],
    [[1],[1],[1],[1],[1],[1],[1]],
    [[1],[1],[0],[1],[1],[1],[1]],
    [[1],[1],[1],[1],[1],[1],[1]],
    [[1],[1],[1],[1],[1],[1],[1]],
     
     
     ]

TESTMATRIX3x10 = [
    [[1],[1],[1],[1],[1],[0],[1],[1],[1],[1]],
    [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],
    [[1],[1],[0],[1],[1],[1],[1],[1],[1],[1]],
    ]

TESTMATRIX9x9 = [
     [[0],[1],[1],[1],[1],[1],[1],[1],[1]],
     [[1],[0],[1],[1],[1],[1],[1],[1],[1]],
     [[1],[1],[0],[1],[1],[1],[1],[1],[1]],
     [[1],[1],[1],[0],[1],[1],[1],[1],[1]],
     [[1],[1],[1],[1],[0],[1],[1],[1],[1]],
     [[1],[1],[1],[1],[1],[0],[1],[1],[1]],
     [[1],[1],[1],[1],[1],[1],[0],[1],[1]],
     [[1],[1],[1],[1],[1],[1],[1],[0],[1]],
     [[1],[1],[1],[1],[1],[1],[1],[1],[0]],   
    
    
    ]

def createnull(width):
    
    zero_row = []
    
    for i in range(0, width):
        zero_row.append([0])
    return zero_row



def nullMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    saved_column = []
    foundZero = False

    for k in range(0, height):
       
        row = matrix[k]
        for i in range(0, width):
            cell = row[i]
            if cell == [0]:
                foundZero = True
                saved_column.append(i)
                
        if foundZero:
            #print(f"found zero in {k} row.")
            newrow = createnull(width)
            matrix[k] = newrow
            #print(matrix[k])
            #print("change made.")
        foundZero = False

    if len(saved_column) > 0:
        for n in range(0, height):
            row = matrix[n]
            for item in saved_column:
                row[item] = [0]

    print("Null matrix function Complete.")
       
def test(matrix):
    print("start null matrix test: original Matrix:")
    for item2 in matrix:
        print(item2)

    nullMatrix(matrix)

    print("---        New NULL matrix  ")
    for item in matrix:
        print(item)
   
    print("*------  END TEST ----------*")
        

#test(TESTMATRIX5x7)
#test(TESTMATRIX3x10)
test(TESTMATRIX9x9)
