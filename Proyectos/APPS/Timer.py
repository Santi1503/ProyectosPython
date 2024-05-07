import tkinter as tk
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        root.update()
        time.sleep(1)
        t -= 1
    label.config(text="READY")

def start_countdown():
    t = int(entry.get())
    countdown(t)

root = tk.Tk()
root.title("Digital Clock")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

entry_label = tk.Label(frame, text="Enter the timer in seconds:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

start_button = tk.Button(frame, text="Start", command=start_countdown)
start_button.grid(row=1, columnspan=2)

label = tk.Label(root, font=("Helvetica", 48), text="00:00")
label.pack(pady=20)

root.mainloop()
