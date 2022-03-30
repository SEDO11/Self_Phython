# 팰린드롬 확인, 앞 부터 읽으나 뒤 부터 읽으나 똑같은 단어

string = input()
list_s = list(string) # 리스트에 단어를 하나씩 대입
s1 = ""
s2 = ""

for i in list_s:
    s1 += i # 문자열에 문자 하나씩 대입

list_s.reverse() # 리스트 요소 반대로 전환
for i in list_s:
    s2 += i # 문자열에 문자 하나씩 대입
    
if s1 == s2: # 팰린트롬인 경우
    print(1) 
else : # 팰린트롬이 아닌 경우
    print(0)
