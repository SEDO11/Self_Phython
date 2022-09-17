import speech_recognition as sr
import pyttsx3
from selenium import webdriver
import time

def webConnection(name):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36") # 봇 우회
    browser = webdriver.Chrome('C:/j/chromedriver.exe', options=options)
    browser.maximize_window()
    browser.get(f'https://www.{name}.com')
    time.sleep(10)

listener = sr.Recognizer()
engine = pyttsx3.init() # 라이브러리 초기화
engine.say('안녕하세요 저는 알렉사에요') # 
engine.say('원하는 걸 말씀하세요')
engine.runAndWait()
try: # 마이크나 다른것에서 오류가 발생 될 수 있으므로 예외 처리
    with sr.Microphone() as source: # 마이크를 이용해 음성 듣기
        print('듣는 중...') # 듣는 중
        voice = listener.listen(source) # 음성 듣기
        command = listener.recognize_google(voice, language='ko-KR') # 음성 언어 설정
        if '유튜브' in command: 
            engine.say('유튜브를 켜드릴게요')
            engine.runAndWait()
            print('유튜브에 접속합니다.')
            webConnection('youtube')
            
        elif '네이버' in command: 
            engine.say('네이버를 켜드릴게요')
            engine.runAndWait()
            print('네이버에 접속합니다.')
            webConnection('naver')
            
        elif '넷플릭스' in command: 
            engine.say('넷플릭스를 켜드릴게요')
            engine.runAndWait()
            print('넷플릭스에 접속합니다.')
            webConnection('netflix')
            
        elif '쿠팡' in command: 
            engine.say('쿠팡을 켜드릴게요')
            engine.runAndWait()
            print('쿠팡에 접속합니다.')
            webConnection('coupang')
except:
    pass
finally:
    print('종료')
    