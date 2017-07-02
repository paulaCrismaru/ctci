import unittest


def is_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    index_a = -1
    index_b = 0
    found_start = False
    while True:
        if not found_start and index_a == len(string_a):
                return False
        else:
            if string_a[index_a % len(string_a)] == string_b[index_b % len(string_b)]:
                index_b += 1
                found_start = True
            else:
                found_start = False
                index_b -= 1
        index_a += 1
        if index_b == len(string_a) - 1:
            break
    return True


class Test(unittest.TestCase):

    good_a = "aaaaaaaaaaaaaaaaaaaaaaaaabc"
    good_b = "aaaaaaaaaaaaaaaaaaaaaaaabca"
    bad_a = "aAav"
    bad_b = "asdf"

    def test_is_permutation(self):
        self.assertEqual(is_permutation(self.good_a, self.good_b), True)
        self.assertEqual(is_permutation(self.bad_a, self.bad_b), False)

if __name__ == "__main__":
    unittest.main()
