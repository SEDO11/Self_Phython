## tkinter를 tk로 선언
import tkinter as tk

## Tk setup
root = tk.Tk()
# GUI Window 사이즈 설정
root.geometry('1000x500')
root.title('완전한 GUI 프로그래밍')
root.resizable(False, False)

# 상단 프레임 (Pack 사용)
frame_top = tk.Frame(root)
frame_top.pack(side="top")

entry = tk.Entry(frame_top, width=22)
entry.pack(side="left")
btn_clear = tk.Button(frame_top, text="지우기", width=10)
btn_clear.pack(side="right")

# 하단 프레임 (Grid 사용)
frame_bot = tk.Frame(root)
frame_bot.pack(side="top")

btn_min = tk.Button(frame_bot, text="-", width=10)
btn_plus = tk.Button(frame_bot, text="+", width=10)
btn0 = tk.Button(frame_bot, text="0", width=10)
btn1 = tk.Button(frame_bot, text="1", width=10)
btn2 = tk.Button(frame_bot, text="2", width=10)
btn3 = tk.Button(frame_bot, text="3", width=10)
btn4 = tk.Button(frame_bot, text="4", width=10)
btn5 = tk.Button(frame_bot, text="5", width=10)
btn6 = tk.Button(frame_bot, text="6", width=10)
btn7 = tk.Button(frame_bot, text="7", width=10)
btn8 = tk.Button(frame_bot, text="8", width=10)
btn9 = tk.Button(frame_bot, text="9", width=10)

# 더하기 빼기 버튼 위치(Grid)
btn_min.grid(row=4, column=1)
btn_plus.grid(row=4, column=3)

btn0.grid(row=4, column=2)
btn1.grid(row=3, column=1)
btn2.grid(row=3, column=2)
btn3.grid(row=3, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)
root.mainloop()