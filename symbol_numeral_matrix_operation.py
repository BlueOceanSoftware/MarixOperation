# matrix/list_matrix.py
# 2025-12-31
# 2026-01-01

class SymbolMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.shape = None

        rows = len(self.matrix)
        cols = len(self.matrix[0]) if rows > 0 else 0
        
        for i in range(1,len(self.matrix)):
            if len(self.matrix[i]) != cols:
                return None
        self.shape = (rows, cols)

def SymbolMatrix_multiply(X, Y):
    if X.shape[1] != Y.shape[0]:
        raise ValueError("Incompatible matrix sizes for multiplication")
    result = []
    for i in range(X.shape[0]):
        row = []
        for j in range(Y.shape[1]):
            # xij
            xij = ''
            for k in range(X.shape[1]):
                splus= '' if k==0 else '+'
                xij += splus + X.matrix[i][k] + '' + Y.matrix[k][j]
            row.append(xij)
        result.append(row)
    return result

A= [['A', 'B'],
    ['C', 'D']]
B = [['a', 'b', 'c'], 
     ['d', 'e', 'f']]
print(A, B)

a = SymbolMatrix(A)
b = SymbolMatrix(B)

print(a.shape)
print(b.shape)

print("multiply symbol matrix:", A, "*", B, "=", SymbolMatrix_multiply(a, b))

def NumeralMatrix_multiply(X, Y):
    result = []
    for i in range(len(X)):
        result_row = []
        for j in range(len(Y[0])):
            sum_product = 0
            for k in range(len(Y)):
                sum_product += X[i][k] * Y[k][j]
            result_row.append(sum_product)
        result.append(result_row)
    return result

# Example usage:
A = [[1, 2], 
     [3, 4]]
B = [[5, 6, 7], 
     [8, 9, 10]]
C = NumeralMatrix_multiply(A, B) 
print("multiply numeral matrix:", A, "*", B, "=", NumeralMatrix_multiply(A, B))
