class MatrixContentError(Exception):
    """Raised when the matrix contains non-integer values."""
    pass

class MatrixSizeError(Exception):
    """Raised when the matrix is not a perfect square."""
    pass

def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().strip()
    if not line:
        break

    row = line.split()

    try:
        row = [int(x) for x in row]
    except ValueError:
        raise MatrixContentError("The matrix must consist of only integers")

    mtrx.append(row)

size = len(mtrx)
if any(len(row) != size for row in mtrx):
    raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row)
