def reverseLookup(dictionary, target):
    key_list = []
    for key, value in dictionary.items():
        if value == target:
            key_list.append(key)
    return key_list


# multiple keys
assert reverseLookup({"a": 1, "b": 1, "c": 1}, 1) == ['a', 'b', 'c']
# single key
assert reverseLookup({"a": 1, "b": 2, "c": 2}, 1) == ['a']
# no keys
assert reverseLookup({"a": 2, "b": 2, "c": 2}, 1) == []