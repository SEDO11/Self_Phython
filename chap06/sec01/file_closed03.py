try:
    file = open("info.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)
finally:
    file.close()
print("파일이 닫혔는가?> ", file.closed)