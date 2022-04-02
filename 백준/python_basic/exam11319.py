#자음 모음 세기, 모음 [’A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’]

run = int(input())
list_vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

for i in range(run):
    string = input()
    result = string.replace(" ", "") # 공백제거
    vow = 0
    for j in range(len(result)):
        if result[j] in list_vowel:
            vow += 1
    cons = len(result) - vow
    print(cons, vow)
