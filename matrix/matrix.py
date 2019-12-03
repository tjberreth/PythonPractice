
class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = Matrix._parse_matrix(matrix_string)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return list(map(lambda xs: xs[index - 1], self.matrix))

    @staticmethod
    def _parse_matrix(matrix_string):
        def parse_column(row_string):
            return list(map(int, row_string.split()))
        return list(map(parse_column, matrix_string.splitlines()))