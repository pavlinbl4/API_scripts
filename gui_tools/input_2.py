import tkinter as tk


class InputWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Input Data")

        self.label_name = tk.Label(self, text="Name")
        self.label_name.pack()

        self.entry_name = tk.Entry(self)
        self.entry_name.pack()

        self.label_age = tk.Label(self, text="Age")
        self.label_age.pack()

        self.entry_age = tk.Entry(self)
        self.entry_age.pack()

        self.button_submit = tk.Button(self, text="Submit", command=self.submit_data)
        self.button_submit.pack(side="left")

        self.button_close = tk.Button(self, text="Close", command=self.close_window)
        self.button_close.pack(side="right")

    def submit_data(self):
        name = self.entry_name.get()
        age = self.entry_age.get()

        # You can do something with the input data here

        self.close_window()
        return age, name

    def close_window(self):
        self.destroy()


input_window = InputWindow()

input_window.mainloop()

print(InputWindow().submit_data())
