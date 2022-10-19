# 텍스트파일 내용 입력
def text_file(filename, text):
    try:
        file = open(filename, "w")
        return file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
text_file("test1.txt", "헬로")