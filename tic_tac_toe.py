import tkinter.messagebox
from tkinter import *
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")
#root.geometry("1350x750+0+0")
root.title("Tic-Tac-Toe")
root.configure(background="Cadet Blue")

Tops=Frame(root, bg='Cadet Blue',  width=1350, pady=2, height=100, relief=RIDGE)
Tops.grid(row=0,column=0)

lblTitle=Label(Tops, font=('Arial',50,'bold'), text="Advanced Tic Tac Toe Game", bd=21,bg="Cadet Blue",fg="Cornsilk",justify=CENTER)
lblTitle.grid(row=0, column=0)

Mainframe=Frame(root, bg='Powder Blue', bd=10, width=1350, relief=RIDGE)
Mainframe.grid(row=1,column=0)

Leftframe=Frame(Mainframe, bg='Cadet Blue', bd=10, padx=10, pady=2, width=750, height=500, relief=RIDGE)
Leftframe.pack(side=LEFT)

Rightframe=Frame(Mainframe, bg='Cadet Blue', bd=10, padx=10, pady=2, width=560, height=500, relief=RIDGE)
Rightframe.pack(side=RIGHT)

Rightframe1=Frame(Rightframe, bg='Cadet Blue', bd=10, padx=10, pady=2, width=400, height=200, relief=RIDGE)
Rightframe1.grid(row=0, column=0)

Rightframe2=Frame(Rightframe, bg='Cadet Blue', bd=10, padx=10, pady=2, width=400, height=200, relief=RIDGE)
Rightframe2.grid(row=1, column=0)

PlayerX=IntVar()
PlayerO=IntVar()
PlayerX.set(0)
PlayerO.set(0)

buttons=StringVar()
click=True
count=0
def checker(buttons):
    global click
    global count
    if buttons["text"]== " " and click==True:
        buttons["text"]="X"
        click=False
        count+=1
        scorekeeper()
    elif buttons["text"]==" " and click==False:
        buttons["text"]="O"
        click=True
        count+=1
        scorekeeper()
    else:
        messagebox.showerror('Tic Tac Toe','Hey! That box has already been selected.\nPick another box')
        
def disable_all_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
        
def scorekeeper():
    global winner
    winner=False
    global count
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X'):
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button4['text']=='X' and button5['text']=='X' and button6['text']=='X'):
        button4.configure(background='powder blue')
        button5.configure(background='powder blue')
        button6.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button7['text']=='X' and button8['text']=='X' and button9['text']=='X'):
        button7.configure(background='powder blue')
        button8.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button1['text']=='X' and button4['text']=='X' and button7['text']=='X'):
        button1.configure(background='powder blue')
        button4.configure(background='powder blue')
        button7.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button2['text']=='X' and button5['text']=='X' and button8['text']=='X'):
        button2.configure(background='powder blue')
        button5.configure(background='powder blue')
        button8.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button3['text']=='X' and button6['text']=='X' and button9['text']=='X'):
        button3.configure(background='powder blue')
        button6.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button1['text']=='X' and button5['text']=='X' and button9['text']=='X'):
        button1.configure(background='powder blue')
        button5.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
        button3.configure(background='powder blue')
        button5.configure(background='powder blue')
        button7.configure(background='powder blue')
        n=float(PlayerX.get())
        score=n+1
        PlayerX.set(score)
        winner=True
        messagebox.showinfo('WINNER','X has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button1['text']=='O' and button2['text']=='O' and button3['text']=='O'):
        button1.configure(background='powder blue')
        button2.configure(background='powder blue')
        button3.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button4['text']=='O' and button5['text']=='O' and button6['text']=='O'):
        button4.configure(background='powder blue')
        button5.configure(background='powder blue')
        button6.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button7['text']=='O' and button8['text']=='O' and button9['text']=='O'):
        button7.configure(background='powder blue')
        button8.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button1['text']=='O' and button4['text']=='O' and button7['text']=='O'):
        button1.configure(background='powder blue')
        button4.configure(background='powder blue')
        button7.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button2['text']=='O' and button5['text']=='O' and button8['text']=='O'):
        button2.configure(background='powder blue')
        button5.configure(background='powder blue')
        button8.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button3['text']=='O' and button6['text']=='O' and button9['text']=='O'):
        button3.configure(background='powder blue')
        button6.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
    
    elif(button1['text']=='O' and button5['text']=='O' and button9['text']=='O'):
        button1.configure(background='powder blue')
        button5.configure(background='powder blue')
        button9.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif(button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        button3.configure(background='powder blue')
        button5.configure(background='powder blue')
        button7.configure(background='powder blue')
        n=float(PlayerO.get())
        score=n+1
        PlayerO.set(score)
        winner=True
        messagebox.showinfo('WINNER','O has won the game\nCongratulations!')
        count=0
        disable_all_buttons()
        
    elif count==9 and winner==False:
        messagebox.showinfo('Tic Tac Toe', 'Its a Draw\nNobody Wins')
        disable_all_buttons()
        
        
        
def reset():
    
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "
    
    button1.config(state=ACTIVE)
    button2.config(state=ACTIVE)
    button3.config(state=ACTIVE)
    button4.config(state=ACTIVE)
    button5.config(state=ACTIVE)
    button6.config(state=ACTIVE)
    button7.config(state=ACTIVE)
    button8.config(state=ACTIVE)
    button9.config(state=ACTIVE)
    
    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')
def newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

lblPlayerX=Label(Rightframe1, font=('Arial',40,'bold'), text="Player X:", padx=2, pady=2,bg="Cadet Blue")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX=Entry(Rightframe1, font=('Arial',40,'bold'), textvariable=PlayerX, bd=2, fg='black', width=14, justify=LEFT)
txtPlayerX.grid(row=0, column=1)

lblPlayerO=Label(Rightframe1, font=('Arial',40,'bold'), text="Player O:", padx=2, pady=2,bg="Cadet Blue")
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO=Entry(Rightframe1, font=('Arial',40,'bold'), textvariable=PlayerO, bd=2, fg='black', width=14, justify=LEFT)
txtPlayerO.grid(row=1, column=1)

btnReset=Button(Rightframe2, text="Reset", font=("Arial", 40, "bold"), height=1, width=20, command=reset)
btnReset.grid(row=0, column=0, padx=6, pady=10)

btnNewGame=Button(Rightframe2, text="New Game", font=("Arial", 40, "bold"), height=1, width=20, command=newgame)
btnNewGame.grid(row=1, column=0, padx=6, pady=11)

button1=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button1))
button1.grid(row=0, column=0, sticky=S+N+E+W)

button2=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button2))
button2.grid(row=0, column=1, sticky=S+N+E+W)

button3=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button3))
button3.grid(row=0, column=2, sticky=S+N+E+W)

button4=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button4))
button4.grid(row=1, column=0, sticky=S+N+E+W)

button5=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button5))
button5.grid(row=1, column=1, sticky=S+N+E+W)

button6=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button6))
button6.grid(row=1, column=2, sticky=S+N+E+W)

button7=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button7))
button7.grid(row=2, column=0, sticky=S+N+E+W)

button8=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button8))
button8.grid(row=2, column=1, sticky=S+N+E+W)

button9=Button(Leftframe, text=" ", font=("Times", 26, "bold"), height=3, width=8, bg="gainsboro", command=lambda:checker(button9))
button9.grid(row=2, column=2, sticky=S+N+E+W)

root.mainloop()