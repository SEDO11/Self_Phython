#알파벳 찾기

d = ["a", "b", "c", "d", "e", "f", "g", 
     "h", "i", "j", "k", "l", "m", "n", 
     "o", "p", "q", "r", "s", "t", "u", 
     "v", "w", "x", "y", "z"]

s = input()

for i in d:
    index = s.find(i)
    print(index, end=" ")
    
    
# 다른분의 모범 답안
word = input()
for i in range(97,123): # ascii code 소문자 a~z
    print(word.find(chr(i)), end=' ')  