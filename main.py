import tkinter as tk

# ---------- Functions ----------
expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# ---------- Window ----------
root = tk.Tk()
root.title("🐉 Red Dragon Calculator")
root.geometry("380x600")
root.configure(bg="#3b0000")

equation = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=equation,
    font=("Consolas", 24),
    bg="#5a0000",
    fg="#ffcccb",
    bd=8,
    relief="ridge",
    justify="right"
)
display.pack(fill="x", padx=15, pady=15)

# ---------- Dragon ----------
dragon = tk.Canvas(root, width=340, height=180,
                   bg="#3b0000", highlightthickness=0)
dragon.pack()

# Wings
dragon.create_polygon(80,80,30,40,60,120, fill="#990000", outline="")
dragon.create_polygon(260,80,310,40,280,120, fill="#990000", outline="")

# Body
dragon.create_oval(100,40,240,150, fill="red", outline="darkred", width=4)

# Eyes
dragon.create_oval(140,75,150,85, fill="white")
dragon.create_oval(190,75,200,85, fill="white")
dragon.create_oval(144,78,148,82, fill="black")
dragon.create_oval(194,78,198,82, fill="black")

# Horns
dragon.create_polygon(125,40,140,10,150,40, fill="gold")
dragon.create_polygon(190,40,200,10,215,40, fill="gold")

# Smile
dragon.create_arc(140,90,200,120,start=180,extent=180,
                  style=tk.ARC,width=3,outline="white")

dragon.create_text(
    170,160,
    text="🔥 Dragon Calculator 🔥",
    fill="gold",
    font=("Arial",16,"bold")
)

# ---------- Buttons ----------
frame = tk.Frame(root, bg="#3b0000")
frame.pack(pady=10)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['C','0','=','+']
]

for r,row in enumerate(buttons):
    for c,text in enumerate(row):

        if text == "=":
            cmd = equal
        elif text == "C":
            cmd = clear
        else:
            cmd = lambda t=text: press(t)

        tk.Button(
            frame,
            text=text,
            command=cmd,
            font=("Arial",18,"bold"),
            width=5,
            height=2,
            bg="#8B0000",
            fg="white",
            activebackground="#ff3333",
            relief="raised"
        ).grid(row=r,column=c,padx=5,pady=5)

root.mainloop()