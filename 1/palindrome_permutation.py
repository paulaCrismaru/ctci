import unittest


def palindmrome_permutation(my_string):
    letters = [0] * 26
    for char in my_string:
        if char.isalpha():
            letters[ord(char.lower()) - 97] += 1
    odd_count = 0
    for letter_count in letters:
        if letter_count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


class Test(unittest.TestCase):

    good_string = "tact coa"
    bad_string = "aabbcd"

    def test_palindrome_permutation(self):
        self.assertTrue(palindmrome_permutation(self.good_string))
        self.assertFalse(palindmrome_permutation(self.bad_string))


if __name__ == "__main__":
    unittest.main()
