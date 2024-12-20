import tkinter

window = tkinter.Tk()
window.title("Calculator")
window.geometry("390x500")
window.resizable(0, 0)
window.config(bg="gray13")

sample_text = tkinter.Entry(window, width=13, font=("arial", 35), fg="white", bg="gray3")
sample_text.pack()


def set_text(value):
    sample_text.insert("end", value)


def reset():
    sample_text.delete(0, "end")


def delete():
    text = sample_text.get()
    sample_text.delete(0, "end")
    sample_text.insert(0, text[:-1])


def result(event=None):
    try:
        res = eval(sample_text.get())
        sample_text.delete(0, "end")
        sample_text.insert(0, res)
    except Exception:
        sample_text.delete(0, "end")
        sample_text.insert(0, "Error")


window.bind('<Return>', result)

buttons = [
    ("1", 20, 285, lambda: set_text("1")),
    ("2", 107, 285, lambda: set_text("2")),
    ("3", 193, 285, lambda: set_text("3")),
    ("4", 20, 220, lambda: set_text("4")),
    ("5", 107, 220, lambda: set_text("5")),
    ("6", 193, 220, lambda: set_text("6")),
    ("7", 20, 155, lambda: set_text("7")),
    ("8", 107, 155, lambda: set_text("8")),
    ("9", 193, 155, lambda: set_text("9")),
    ("0", 107, 350, lambda: set_text("0")),
    (".", 193, 350, lambda: set_text(".")),
    ("+", 280, 350, lambda: set_text("+")),
    ("-", 280, 285, lambda: set_text("-")),
    ("*", 280, 220, lambda: set_text("*")),
    ("/", 280, 155, lambda: set_text("/")),
    ("C", 20, 350, reset),
    ("←", 280, 415, delete),
    ("=", 107, 415, result),
]

for text, x, y, command in buttons:
    tkinter.Button(
        window, text=text, width=4, height=1, font=("arial", 20, "bold"),
        bd=1, fg="white", bg="gray35" if text.isdigit() or text == "." else "darkorange",
        command=command
    ).place(x=x, y=y)

window.mainloop()
