def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list: #item이 리스트일 경우
            result += flatten(item)
            print("true:", result)
        else: #아닐 경우
            result += [item]
            print("else:", result)
    return result

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(example)
print(flatten(example))