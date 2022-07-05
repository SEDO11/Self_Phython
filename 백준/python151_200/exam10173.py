#니모를 찾아서
# 내가 작성한 코드
while True:
    s = input()
    if s == "EOI":
        break
    s = s.lower()
    t = 0
    if "nemo" in s:
        print("Found")
    else:
        print("Missing")

# 좋은 코드
while True:
    s = input()
    if s == "EOI":
        break
    s = s.lower()
    print("Found" if "nemo" in s else "Missing")