import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

app = ctk.CTk()
app.title('Calculator')
app.geometry('300x275')
app.configure(bg='#000')

font1 = ('Arial', 20, 'bold')

input = ctk.CTkEntry(app, font=font1, text_color='black', fg_color='#fff', border_color='#000', width=280, height=50)
input.place(x=10, y=10)

btn1 = ctk.CTkButton(app, command=lambda: button_click('7'), font=font1, text_color= '#fff', text='7', fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
btn1.place(x=10, y=80)

app.mainloop()