#이름 성적 출력

run = int(input())
for i in range(run):
    student = input().split()
    score = int(student[1])
    scroe_result = ""
    if score >= 97:
        score_result = "A+"
    elif score >= 90:
        score_result = "A"
    elif score >= 87:
        score_result = "B+"
    elif score >= 80:
        score_result = "B"
    elif score >= 77:
        score_result = "C+"
    elif score >= 70:
        score_result = "C"
    elif score >= 67:
        score_result = "D+"
    elif score >= 60:
        score_result = "D"
    else :
        score_result = "F"
    result = student[0] + " " + score_result
    print(result)