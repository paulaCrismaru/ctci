import unittest


def one_away(string_a, string_b):
    if abs(len(string_a) - len(string_b)) > 1:
        return False
    if string_a == string_b:
        return True
    diffs = 0
    index_a = 0
    index_b = 0
    while True:
        if string_a[index_a] == string_b[index_b]:
            index_a += 1
            index_b += 1
        elif len(string_a) == len(string_b):
            index_a += 1
            index_b += 1
            diffs += 1
        elif len(string_a) > len(string_b):
            index_a += 1
            diffs += 1
        else:
            index_b += 1
            diffs += 1
        if diffs > 1:
            return False
        if index_a == len(string_a) or index_b == len(string_b):
            break
    return True


class Test(unittest.TestCase):

    good_str_a_1 = "pale"
    good_str_b_1 = "ple"
    good_str_a_2 = "pales"
    good_str_b_2 = "pale"
    good_str_a_3 = "pale"
    good_str_b_3 = "bale"
    bad_str_a_4 = "pale"
    bad_str_b_4 = "bake"

    def test(self):
        self.assertTrue(one_away(self.good_str_a_1, self.good_str_b_1))
        self.assertTrue(one_away(self.good_str_a_2, self.good_str_b_2))
        self.assertTrue(one_away(self.good_str_a_3, self.good_str_b_3))
        self.assertFalse(one_away(self.bad_str_a_4, self.bad_str_b_4))


if __name__ == "__main__":
    unittest.main()
