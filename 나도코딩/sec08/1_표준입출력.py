import sys

print("python", "java", sep=" vs ", end="?\n")
print("무엇이 더 재미있을까요?")

print("python", "java", file=sys.stdout) # 표준 출력처리
print("python", "java", file=sys.stderr) # 표준 에러처리

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # 키와 값으로 나눠서 변수에 저장
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    
# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호: "+str(num).zfill(3)) # 빈 칸을 0으로 채워줌

