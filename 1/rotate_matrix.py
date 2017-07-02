import unittest


def rotate_matrix(m):
    i = j = 0
    n = len(m)
    while True:
        aux1 = m[j][n - i - 1]
        m[j][n - i - 1] = m[i][j]

        aux2 = m[n - i - 1][n - j - 1]
        m[n - i - 1][n - j - 1] = aux1

        aux1 = m[n - j - 1][i]
        m[n - j - 1][i] = aux2

        m[i][j] = aux1

        if j != n - 2 - i:
            j += 1
        else:
            i += 1
            j = i
        if i == n / 2:
            break
    return m


class Test(unittest.TestCase):

    input_1 = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36]
    ]
    output_1 = [
        [31, 25, 19, 13, 7, 1],
        [32, 26, 20, 14, 8, 2],
        [33, 27, 21, 15, 9, 3],
        [34, 28, 22, 16, 10, 4],
        [35, 29, 23, 17, 11, 5],
        [36, 30, 24, 18, 12, 6]
    ]

    input_2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    output_2 = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix(self.input_1), self.output_1)
        self.assertEqual(rotate_matrix(self.input_2), self.output_2)


if __name__ == "__main__":
    unittest.main()

