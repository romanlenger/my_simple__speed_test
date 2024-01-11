from tkinter import *
import tkinter as tk
from tkinter import ttk
from speedtest import Speedtest
from tkinter import Canvas
from tqdm import tqdm
import time
import threading


def animate_rectangle(rect, width):
    steps = 100

    for i in range(steps + 1):
        rect_width = i * (width / steps)
        progress_bar.coords(rect, 0, 0, rect_width, progress_bar.winfo_reqheight())
        root.update_idletasks()
        time.sleep(0.18)


def start_test():
    download_label.config(text='Download speed:\nTesting...')
    upload_label.config(text='Upload speed:\nTesting...')
    
    st = Speedtest()
    download = st.download()
    upload = st.upload()

    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text=f'Download speed:\n{download_speed} MbPs')
    upload_label.config(text=f'Upload speed:\n{upload_speed} MbPs')


def on_start_button_click():
    rect = progress_bar.create_rectangle(0, 0, 0, progress_bar.winfo_reqheight(), fill="green") 
    width = progress_bar.winfo_reqwidth()  
    threading.Thread(target=start_test).start()
    threading.Thread(target=animate_rectangle, args=(rect, width)).start()
    

root = Tk()

root.title('Speed Test')
root.geometry('350x400')

style = ttk.Style()
style.configure("TButton", padding=8, relief="flat", background="lightblue", foreground="black", font=('Helvetica', 14, 'bold'))

button = ttk.Button(root, text='Start', command=on_start_button_click, style="TButton")
button.pack(side=BOTTOM, pady=60)

download_label = Label(root, text='Download speed:\n-', font=40)
download_label.pack(pady=(30, 0))

upload_label = Label(root, text='Upload speed:\n-', font=30)
upload_label.pack(pady=10)

progress_bar = tk.Canvas(root, width=200, height=30, bg="gray", highlightthickness=0)
progress_bar.pack(pady=20)

root.mainloop()
