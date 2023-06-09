import tkinter as tk


def get_input_data():
    # Create a new Tkinter window
    input_window = tk.Tk()

    # Set the title of the window
    input_window.title("Input Data")
    input_window.resizable(False, False)
    
    # Добавляем логику чтобы окно было по центру экрана
    window_height = 100
    window_width = 300
    screen_width = input_window.winfo_screenwidth()
    screen_height = input_window.winfo_screenheight()
    x = int(screen_width / 4 - window_width / 2)
    y = int(screen_height / 2 - window_height / 2)
    input_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a label for the input field
    input_label = tk.Label(input_window, text="Enter the data:")
    input_label.pack()

    # Create an entry field for the input data
    input_field = tk.Entry(input_window, width=30)
    input_field.pack()

    # Create a button to submit the data
    submit_button = tk.Button(input_window, text="Submit", command=input_window.quit, height=1, width=10)
    submit_button.pack(side='bottom', pady=10, anchor='center')
    submit_button.pack()

    # Start the main event loop for the window
    input_window.mainloop()

    # Get the entered data from the input field
    input_data = input_field.get()

    # Destroy the window after it has been submitted
    input_window.destroy()

    # Return the entered data
    return input_data


data = get_input_data()
print("The entered data was:", data)
