#파일입출력
# w는 새로 쓴다는 뜻이다
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# a 는 이어서 쓴다는 것이다.
# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80\n")
# score_file.write("과학 : 100")
# score_file.close()

# r은 파일의 내용을 읽어 온다는 뜻이다.
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 한줄씩 출력
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 한 줄만 읽고 커서를 다음 줄로 이동
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# score_file.close()

# 파일의 내용이 몇 줄인지 모를 경우 읽어올 때 
#1
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

#2
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 줄을 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()