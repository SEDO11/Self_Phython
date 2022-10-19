# 리스트 평탄화

def flatten(data):
    lst = []
    for i in data:
        if type(i) == list: # 리스트 형식인경우
            lst += flatten(i) # 재귀함수 실행후  결과 값을 더함
        else: #리스트 형식이 아닌경우
            lst += [i] #더함
    return lst

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(example)
print(flatten(example))