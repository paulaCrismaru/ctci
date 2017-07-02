import unittest


def compress_string(my_string):
    prev_char = ""
    count = 0
    compressed_string = ""
    for char in my_string:
        if char == prev_char:
            count += 1
        else:
            compressed_string += prev_char + str(count)
            count = 1
        prev_char = char
        if len(compressed_string) > len(my_string):
            return my_string
    compressed_string += prev_char + str(count)
    return compressed_string[1:]


class Test(unittest.TestCase):

    input_output = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_compress_string(self):
        for io in self.input_output:
            self.assertEqual(compress_string(io[0]), io[1])

if __name__ == '__main__':
    unittest.main()
