import unittest


def is_string_rotation(string_a, string_b):
    index_a = index_b = 0
    prefix = ''
    while index_a != len(string_a):
        if string_a[index_a] == string_b[index_b]:
            index_a += 1
            index_b += 1
        else:
            index_a = index_a - index_b + 1
            prefix += string_a[index_a - 1]
            index_b = 0
    return is_substring(string_b, prefix)


def is_substring(string_a, string_b):
    return string_b in string_a


class Test(unittest.TestCase):
    data = [
        (('waterbottle', 'erbottlewat'), True),
        (('ababac', 'abacab'), True),
        (('random string', '1234'), False)
    ]

    def test_is_string_rotation(self):
        for data_in, data_out in self.data:
            self.assertEqual(is_string_rotation(*data_in), data_out)


if __name__ == "__main__":
    unittest.main()
