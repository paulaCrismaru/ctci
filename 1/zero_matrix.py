import unittest


def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    lines = [False] * m
    columns = [False] * n
    for line_index in xrange(m):
        for column_index in xrange(n):
            if matrix[line_index][column_index] == 0:
                lines[line_index] = True
                columns[column_index] = True
    for line_index in xrange(m):
        if lines[line_index]:
            for column_index in xrange(n):
                matrix[line_index][column_index] = 0
    for column_index in xrange(n):
        if columns[column_index]:
            for line_index in xrange(len(matrix)):
                matrix[line_index][column_index] = 0
    return matrix


class Test(unittest.TestCase):

    input_1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 0],
        [0, 0, 8, 0]
    ]
    output_1 = [
        [0, 0, 3, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    def test_zero_matrix(self):
        self.assertEqual(zero_matrix(self.input_1), self.output_1)


if __name__ == "__main__":
    unittest.main()
