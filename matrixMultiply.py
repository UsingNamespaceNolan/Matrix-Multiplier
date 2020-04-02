class Matrix:
    def __init__(self):
        pass
    matrix = None
    numRows = 0
    numCols = 0

def inpData(rows, cols):
    matrix = [[None for i in range(cols)] for j in range(rows)]
    for x in range(rows):
        for y in range(cols):
            matrix[x][y] = float(input("Enter row " + str(x+1) + " column " + str(y+1) + " "))
    return matrix

def multiply(matrix1, matrix2):
    prodMatrix = [[None for i in range(matrix2.numCols)] for j in range(matrix1.numRows)]
    placeholder = 0
    for x in range(matrix1.numRows):
        for y in range(matrix2.numCols):
            for z in range(matrix1.numCols):
                placeholder += float(matrix1.matrix[x][z])*float(matrix2.matrix[z][y])
            prodMatrix[x][y] = placeholder
            placeholder = 0
    return prodMatrix

#declaring matrices
matrix1 = Matrix()
matrix1.numRows = int(input("Enter matrix 1 row dimension as an integer: "))
matrix1.numCols = int(input("Enter matrix 1 column dimension as an integer: "))
matrix1.matrix = inpData(matrix1.numRows, matrix1.numCols)

matrix2 = Matrix()
matrix2.numRows = int(input("Enter matrix 2 row dimension as an integer: "))
while matrix1.numCols != matrix2.numRows:
    print("Number of columns of matrix 1 must equal the number of rows of matrix 2")
    matrix2.numRows = int(input("Enter matrix 2 row dimension as an integer: "))
matrix2.numCols = int(input("Enter matrix 2 column dimension as an integer: "))
matrix2.matrix = inpData(matrix2.numRows, matrix2.numCols)

productMatrix = Matrix()
productMatrix.numRows = matrix1.numRows
productMatrix.numCols = matrix2.numCols
productMatrix.matrix = multiply(matrix1, matrix2)

print(productMatrix.matrix)
