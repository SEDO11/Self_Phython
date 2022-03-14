example_list = ["요소A", "요소B", "요소C"]
example_list2 = [["요소A", "요소B", "요소C"], ["요소D", "요소E", "요소F"]]

print(example_list)
print()

print(enumerate(example_list))
print()

print(list(enumerate(example_list)))
print()

# enumerate 쓸경우
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))
print()

for i, value in enumerate(example_list2):
    for j in range(len(value)):
        print("[{}, {}]번째 요소는 입니다. {}".format(i, j, value[j]))
print()

# enumerate 안쓸경우
for i in range(len(example_list)):
    print("{}번째 요소는 {}입니다.".format(i, example_list[i]))
print()