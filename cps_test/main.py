import threading
import time
import tkinter


def click(*args):
    global cps
    cps += 1
    time.sleep(1)
    cps -= 1


win = tkinter.Tk()
win.geometry("300x200")
win.attributes('-type', 'dialog')  # Set the window type to 'dialog'
win.title("CPS Tester")

cps = 0
record = 0

btn = tkinter.Button(win, text="Click Me!", width=100, height=20)
btn.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

lbl = tkinter.Label(win, text="CPS: 0")
rec = tkinter.Label(win, text="RECORD: 0")


def start_click(*args):
    global lbl
    thr = threading.Thread(target=click)
    thr.start()


def upd():
    global record
    lbl.configure(text=f"CPS: {cps}")
    lbl.place(x=0, y=0)
    if cps >= record:
        record = cps
    rec.configure(text=f"RECORD: {record}")
    rec.place(x=0, y=20)
    win.after(10, upd)


btn.bind("<Button-1>", start_click)
upd()

win.mainloop()
