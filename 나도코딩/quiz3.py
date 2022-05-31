#사이트별 비밀번호
# 내가 문자열 자르는 법을 아직 잘 모르는 것 같다
u = input()
u = u.replace("http://", "")
s = u[:u.index(".")]
p = s[:3] + str(len(s)) + str(s.count("e")) + "!"
print("생성된 비밀번호: {}".format(p))