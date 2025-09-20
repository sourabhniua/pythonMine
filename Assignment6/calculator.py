
import tkinter as tk

def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))  
        input_text.set(result)
        expression = result             
    except Exception:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("320x400")

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 18), width=25, bd=5, insertwidth=4, bg="powder blue", justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tk.Frame(root)
btns_frame.pack()

tk.Button(btns_frame, text="7", width=10, height=3, command=lambda: press(7)).grid(row=0, column=0)
tk.Button(btns_frame, text="8", width=10, height=3, command=lambda: press(8)).grid(row=0, column=1)
tk.Button(btns_frame, text="9", width=10, height=3, command=lambda: press(9)).grid(row=0, column=2)
tk.Button(btns_frame, text="/", width=10, height=3, command=lambda: press("/")).grid(row=0, column=3)

tk.Button(btns_frame, text="4", width=10, height=3, command=lambda: press(4)).grid(row=1, column=0)
tk.Button(btns_frame, text="5", width=10, height=3, command=lambda: press(5)).grid(row=1, column=1)
tk.Button(btns_frame, text="6", width=10, height=3, command=lambda: press(6)).grid(row=1, column=2)
tk.Button(btns_frame, text="*", width=10, height=3, command=lambda: press("*")).grid(row=1, column=3)

tk.Button(btns_frame, text="1", width=10, height=3, command=lambda: press(1)).grid(row=2, column=0)
tk.Button(btns_frame, text="2", width=10, height=3, command=lambda: press(2)).grid(row=2, column=1)
tk.Button(btns_frame, text="3", width=10, height=3, command=lambda: press(3)).grid(row=2, column=2)
tk.Button(btns_frame, text="-", width=10, height=3, command=lambda: press("-")).grid(row=2, column=3)

tk.Button(btns_frame, text="0", width=10, height=3, command=lambda: press(0)).grid(row=3, column=0)
tk.Button(btns_frame, text=".", width=10, height=3, command=lambda: press(".")).grid(row=3, column=1)
tk.Button(btns_frame, text="=", width=10, height=3, command=equalpress).grid(row=3, column=2)
tk.Button(btns_frame, text="+", width=10, height=3, command=lambda: press("+")).grid(row=3, column=3)

tk.Button(btns_frame, text="Clear", width=43, height=3, command=clear).grid(row=4, column=0, columnspan=4)

root.mainloop()
