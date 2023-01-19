import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.resizable(False, False)
root.config(background="#dae6f6")

def check_spelling():
    word = enter_text.get()
    isRight = TextBlob(word)
    right = str(isRight.correct())

    correct_spelling = Label(root, text="Correct Spelling is:",font=("poppins", 20), bg="#dae6f6", fg="#364971")
    correct_spelling.place(x=100, y=250)
    spell.config(text=right)

heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))
enter_text = Entry(root, justify="center",width=30, font=("poppins",25),bg="white", fg="black",border=2)
enter_text.pack(pady=10)
enter_text.focus_set()

button = Button(root,text="Check", font=("arial", 20, "bold"), fg="red", bg="white", command=check_spelling)
button.pack()

spell = Label(root,font=("poppins",20),bg="#dae6f6", fg="#364971")
spell.place(x=350,y=250)


root.mainloop()