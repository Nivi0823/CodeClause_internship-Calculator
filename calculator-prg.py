import tkinter as tk
import math


def on_button_click(event):
    text = event.widget.cget("text")
    current_text = entry.get()

    if text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)

        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title(" Scientific Calculator")
root.geometry("400x500")

entry = tk.Entry(root, font=("Helvetica", 24), justify="right", bg="lightblue", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '%'
]

row, col = 1, 0
for button in buttons:
    button = tk.Button(button_frame, text=button, font=("Helvetica", 18), width=5, height=2, bg="lightgreen",
                       fg="black")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()
