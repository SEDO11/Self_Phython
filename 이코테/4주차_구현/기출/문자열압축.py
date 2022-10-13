# 문자열 압축
# 출처: https://ljhyunstory.tistory.com/18 [오늘도 컴돌이!:티스토리]

def solution(s):
    answer = 1000
    if len(s)==1:
        return 1
    for i in range(1, len(s)+1): # 전체 비교
        b = '' # 문자열 저장 변수
        cnt = 1 # 중복 문자열 카운트 변수
        tmp=s[:i] # 첫 글자 저장 변수
        for j in range(i, len(s)+i, i): # n개씩 잘라서 읽음
            if tmp==s[j:i+j]: # 앞글자와 뒷 글자가 같은 경우
                cnt+=1 # 카운트
            else:
                if cnt!=1: # 카운트가 1이 아닌 경우
                    b = b + str(cnt)+tmp # 카운트와 글자를 합쳐서 출력
                else: # 카운트가 1인경우
                    b = b + tmp # 숫자는 필요 없으므로 글자만 출력
                tmp=s[j:j+i] # 뒤의 글자를 비교하기위해 저장
                cnt = 1 # 다시 카운트를 1으로
        answer = min(answer, len(b)) # 자리수가 적은 걸 answer에 저장
    return answer # 가장 작은 자리수 출력

s = input()
r = solution(s)
print(r)