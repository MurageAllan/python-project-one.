from tkinter import *
from tkinter.ttk import *


def start():
    import time
    for i in range(1, 101, 1):
        progress["value"] = i
        root.update_idletasks()
        label1.config(text=str(i)+"%")
        time.sleep(0.1)
    progress["value"] = 100
    root.after(100, main)


def stop():
    root.destroy()

def main():
    root.destroy()
    def Login():
        uname = username.get()
        pwd = password.get()

        if uname == '' or pwd == '':
            message.set("fill in please!!")
        else:
            screen.after(800, Space)
            message.set("welcome")

    def Space():
        screen.destroy()
        window = Tk()
        window.title("Hotel Management System")
        window.geometry("1200x800")

        window.mainloop()

    screen = Tk()
    screen.title("Login Form")
    screen.geometry("300x300")

    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    Label(screen, text="Userame").place(x=20, y=40)
    Entry(screen, textvariable=username).place(x=90, y=42)
    Label(screen, text="Password",).place(x=20, y=80)
    Entry(screen, textvariable=password, show="*").place(x=90, y=82)
    Label(screen, text="", textvariable=message).place(x=100, y=110)
    Button(screen, text="Log in", width=10, command=Login).place(x=105, y=140)

    screen.mainloop()


root = Tk()
root.title("RAEYE")
root.geometry()
root.config(background='#A52A2A')
root.overrideredirect(True)

label1 = Label(root, font="arial 15 bold", foreground="#808080", background="brown")
label1.pack(padx=100, pady=5)

s = Style()
s.configure("TProgressbar")

progress = Progressbar(root, style="TProgressbar", length=400, mode="determinate")
progress.pack(pady=10, padx=10)

button = Button(root, text='start', command=start)
button.pack(pady=10)

stop = Button(root, text='stop', command=stop)
stop.pack(pady=12)



root.mainloop()