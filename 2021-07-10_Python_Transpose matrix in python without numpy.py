#transpose matrix in python without numpy

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T =[]
    for k in range(columns):
        row =[]
        for i in range(rows):
            row.append(matrix[i][k])
        matrix_T.append(row)

    return matrix_T

t = [[1,2,3],
     [4,5,6],
     [7,8,9]]

#printing original Value of Matrix
print(t)
     

print(transpose(t))
     
    
