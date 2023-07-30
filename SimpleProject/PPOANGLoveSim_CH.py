import tkinter
import time

class WindowSetting:
    count=0
    say_hello = "버튼을 눌러주세요"
    close_btn = False
    
    def __init__(self):
        print("")


    def OpenWindow(self, text):
        self.window=tkinter.Tk()
        self.window.title("Game")
        self.window.geometry("900x450+100+100")

        self.variableText = tkinter.StringVar()
        self.variableText.set(self.say_hello)
        self.intro = tkinter.Label(self.window, textvariable = self.variableText).pack()

        self.Make_Hi(text)
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.close_after_id = self.window.after(3000, self.close_window)
        self.window.mainloop()

    def OpenPhoto(self, path):
        self.window=tkinter.Tk()
        self.window.title("Game")
        self.window.geometry("900x450+100+100")

        self.img = tkinter.PhotoImage(file = path,  master=self.window)
        self.img2 = tkinter.PhotoImage(file = "./OLABS_Logo_Black.png",  master=self.window)
        self.label=tkinter.Label(self.window, image=self.img) #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
        self.label.pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.close_after_id = self.window.after(3000, self.close_window)
        self.window.mainloop()
    

    def Make_Hi(self, text):
        count_txt = ""
        for i in text:
            count_txt += i
            self.variableText.set(count_txt)
            self.window.update()
            time.sleep(0.1)

    def close_window(self):
        self.window.destroy()  # 윈도우를 닫는 함수

    def on_closing(self):
        self.cancel_closing()
        self.window.destroy()

    def cancel_closing(self):
        self.window.after_cancel(self.close_after_id)


window = WindowSetting()
count = 1

def countDays():
    window.OpenWindow(f"{count}일 차....")

def openPhotos(path):
    window.OpenPhoto(path)

def openMsgs(msg):
    window.OpenWindow(msg)

if __name__ == '__main__':
    while True:
        countDays()
        msg = input(">> ")
        if msg == "exit":
            break
        if msg == "photo":
            openPhotos("./OLABS_Logo_White.png")
        else:
            openMsgs(msg)
        count += 1