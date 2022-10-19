from tabnanny import check
from xmlrpc.client import boolean


a = input()

check = int(a)

if(check >= 20): {
    print("a는 20 이상입니다.")
} 
elif(check >= 0): {
    print("a는 0 이상 20 미만 입니다.")
} 
else: {
    print("a는 음수 입니다.")
}