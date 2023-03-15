import tkinter as tk

options = []


def choice_address():
    def submit():
        if var1.get() == 1:
            options.append({"Кауровой": "kaurova@kommersant.ru"})
        if var2.get() == 1:
            options.append({"Романова": "romanov@kommersant.ru"})
        if var3.get() == 1:
            options.append({"Лемешевой": "lemesheva@kommersant.ru"})
        if var4.get() == 1:
            options.append({"Кустовой": "kustova@kommersant.ru"})
        if var5.get() == 1:
            options.append({"Соболева": "sobolev_g@kommersant.ru"})
        if var6.get() == 1:
            options.append({"Семенова": "agenty@kommersant.ru"})
        if var7.get() == 1:
            options.append({"Ильюшкиной": "iliyushkina_a@kommersant.ru"})

        root.destroy()

    root = tk.Tk()
    root.title("Выбери адресата")
    root.geometry('300x200')
    root.resizable(False, False)

    # Добавляем логику чтобы окно было по центру экрана
    window_height = 300
    window_width = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int(screen_width / 4 - window_width / 2)
    y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    frame = tk.Frame(root, bd=2)
    frame.place(relx=0.5, rely=0.5, anchor='e')

    var1 = tk.IntVar(value=0)
    var2 = tk.IntVar(value=0)
    var3 = tk.IntVar(value=0)
    var4 = tk.IntVar(value=0)
    var5 = tk.IntVar(value=0)
    var6 = tk.IntVar(value=0)
    var7 = tk.IntVar(value=0)

    checkbutton1 = tk.Checkbutton(frame, text='Кауровой', variable=var1, onvalue=1, offvalue=0)
    checkbutton1.pack(anchor='w')
    checkbutton2 = tk.Checkbutton(frame, text='Романову', variable=var2, onvalue=1, offvalue=0)
    checkbutton2.pack(anchor='w')
    checkbutton3 = tk.Checkbutton(frame, text='Лемешевой', variable=var3, onvalue=1, offvalue=0)
    checkbutton3.pack(anchor='w')
    checkbutton4 = tk.Checkbutton(frame, text='Кустовой', variable=var4, onvalue=1, offvalue=0)
    checkbutton4.pack(anchor='w')
    checkbutton5 = tk.Checkbutton(frame, text='Соболеву', variable=var5, onvalue=1, offvalue=0)
    checkbutton5.pack(anchor='w')
    checkbutton6 = tk.Checkbutton(frame, text='Семенову', variable=var6, onvalue=1, offvalue=0)
    checkbutton6.pack(anchor='w')
    checkbutton7 = tk.Checkbutton(frame, text='Ильюшкиной', variable=var7, onvalue=1, offvalue=0)
    checkbutton7.pack(anchor='w')

    submit_button = tk.Button(frame, text='Submit', command=submit, height=1, width=10)
    submit_button.pack(side='bottom', pady=40, anchor='center')
    root.mainloop()
    return options[0]


if __name__ == '__main__':
    print(choice_address())
