import customtkinter as ctk

class CalcWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x275")
        self.title("Calculator")

class CalendarWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x500")
        self.title("Calendar")

        self.label = ctk.CTkLabel(self, text="Calendar")
        self.label.pack(padx=20, pady=20)

class TodoListWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x800")
        self.title("To Do List")

        self.label = ctk.CTkLabel(self, text="To Do List")
        self.label.pack(padx=20, pady=20)

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
        self.title("Main Window")

        self.btn_calc = ctk.CTkButton(self, text="Calculator", command=self.open_calc)
        self.btn_calc.pack(side="top", padx=20, pady=20)

        self.btn_calendar = ctk.CTkButton(self, text="Calendar", command=self.open_calendar)
        self.btn_calendar.pack(side="top", padx=20, pady=20)

        self.btn_list = ctk.CTkButton(self, text="To Do List", command=self.open_list)
        self.btn_list.pack(side="top", padx=20, pady=20)

        self.calc_window = None
        self.calendar_window = None
        self.list_window = None
    def open_calc(self):
        if self.calc_window is None or not self.calc_window.winfo_exists():
            self.calc_window = CalcWindow(self)
        self.calc_window.lift()
        self.calc_window.focus()
        self.calc_window.attributes('-topmost', True)
        self.calc_window.after(10, lambda: self.calc_window.attributes('-topmost', False))
    def open_calendar(self):
        if self.calendar_window is None or not self.calendar_window.winfo_exists():
            self.calendar_window = CalendarWindow(self)
        self.calendar_window.lift()
        self.calendar_window.focus()
        self.calendar_window.attributes('-topmost', True)
        self.calendar_window.after(10, lambda: self.calendar_window.attributes('-topmost', False))

    def open_list(self):
        if self.list_window is None or not self.list_window.winfo_exists():
            self.list_window = TodoListWindow(self)
        self.list_window.lift()
        self.list_window.focus()
        self.list_window.attributes('-topmost', True)
        self.list_window.after(10, lambda: self.list_window.attributes('-topmost', False))

app = App()
app.mainloop()


