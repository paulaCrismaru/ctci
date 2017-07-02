import unittest


def urlfy(my_string, true_lenght):
    put_space = False
    new_string = ''
    index_char = 0
    spaces_no = 0
    while True:
        if put_space:
            new_string += '%20'
        if (my_string[index_char] == ' ' and
                index_char > 0 and my_string[index_char - 1] != ' '):
                put_space = True
                spaces_no += 2
        else:
            new_string += my_string[index_char]
            put_space = False
            if len(new_string) - spaces_no == true_lenght:
                break
        index_char += 1
    return new_string


class TestUrlfy(unittest.TestCase):

    input_string = "Mr John Smith           "
    n = 13
    expected_string = "Mr%20John%20Smith"

    def test(self):
        self.assertEqual(
            urlfy(self.input_string, self.n), self.expected_string)

if __name__ == '__main__':
    unittest.main()