from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter import *

root = Tk()
root.title("text editor")

def open_file():
    textfield.delete("1.0", END)
    file = askopenfile(mode="r", filetypes=[("text files", "*.txt")])
    if file is not None:
        content = file.read()
        textfield.insert("1.0", content)

def save_file():
    content = textfield.get("1.0", "end-1c")
    file = asksaveasfilename(title="Save", filetypes=[("text files", "*.txt")])
    with open(file, "w") as data:
        data.write(content)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="save", command=save_file)
filemenu.add_command(label="open", command=open_file)
filemenu.add_command(label="exit", command=root.destroy)

textfield = Text(root, font=("sans serif", 10))
textfield.pack()

root.config(menu=menubar)
root.mainloop()