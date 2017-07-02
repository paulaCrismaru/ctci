def _has_unique_characters(my_string):
    """O(N2)"""
    for char in my_string:
        if my_string.count(char) > 1:
            return False
    return True


def __has_unique_characters(my_string):
    chars = []


def has_unique_characters(my_string):
    """with hash O(n)"""
    hashes = [[]] * 10
    for char in my_string:
        hash_ = hash(char)
        hash_index = hash_ % 10
        for h in hashes[hash_index]:
            if hash_ == h:
                return False
        hashes[hash_index].append(hash_)
    return True


good_string = "qwertyuiopasdfghjklzxcvbnm`1234567890-=[]\;',./~!@#$%^&*()_+{}|:<>?"
bad_string = good_string + "?"
print has_unique_characters(bad_string)
print has_unique_characters(good_string)
