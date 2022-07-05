# 보고서 자동 작성

for i in range(1, 51):
    with open(str(i)+"주차.txt","w", encoding="utf-8") as company_file:
        company_file.write("- {} 주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : ".format(i))