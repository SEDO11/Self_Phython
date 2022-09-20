import speech_recognition as sr
import pyttsx3
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36") # 봇 우회
browser = webdriver.Chrome('C:/j/chromedriver.exe', options=options)

def webConnection(name):
    browser.maximize_window()
    browser.get(f'https://www.{name}.com')

listener = sr.Recognizer()
engine = pyttsx3.init() # 라이브러리 초기화
voices = engine.getProperty('voices') # 말 할때 까지 기다려줌
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text) 
    engine.runAndWait()
print('웹 상태 확인', browser)
talk('안녕하세요 저는 알렉사에요, 원하는 것을 말씀하세요')
try: # 마이크나 다른것에서 오류가 발생 될 수 있으므로 예외 처리
    # with sr.Microphone() as source: # 마이크를 이용해 음성 듣기
    #     print('듣는 중...') # 듣는 중
        # voice = listener.listen(source) # 음성 듣기
        # command = listener.recognize_google(voice, language='ko-KR') # 음성 언어 설정
    command = input()
    if '유튜브' in command: 
        talk('유튜브에 접속합니다.')
        print('유튜브에 접속합니다.')
        webConnection('youtube')
        
    elif '네이버' in command: 
        talk('네이버에 접속합니다.')
        print('네이버에 접속합니다.')
        webConnection('naver')
        
    elif '넷플릭스' in command: 
        talk('넷플릭스에 접속합니다.')
        print('넷플릭스에 접속합니다.')
        webConnection('netflix')
        
    elif '쿠팡' in command: 
        talk('쿠팡에 접속합니다.')
        print('쿠팡에 접속합니다.')
        webConnection('coupang')
except:
    pass
finally:
    print('종료')