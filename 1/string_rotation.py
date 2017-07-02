def is_string_rotation(string_a, string_b):

    index_a = 0
    index_b = 0
    string_prefix = ''
    string_suffix = ''
    while string_a[index_a] != string_b[index_b] and index_a < len(string_a) - 1:
        string_prefix += string_b[index_b]
        index_b += 1

    for i in xrange(index_b, len(string_b)):
        string_suffix += string_b[i]
    print string_prefix
    print string_suffix
    return isSubstring(string_suffix, string_a)


def isSubstring(a, b):

    return a in b

a = "waterbottle"
b = "erbottlewat"
a = "ababac"
b = "abacab"
print is_string_rotation(a, b)
