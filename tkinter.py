##tkinter class by sam
import tkinter as tk
import tkinter.ttk as ttk ##little softer
##Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):
##Tk gives us the window
##tk.Tk()##bad practise
##better practise down
win=tk.Tk()##win is  a object

expr=""
text=tk.StringVar()##grabs info that u r passing to it , like a cursor

def press(num):
    global expr
    expr+=str(num)  ##think whats happening here
    text.set(expr)##with tkinter variables you cannot do tkinterVar=value , we have to do like tkinterVar.set(value)


##widget ==object==window for this
win.title("ganesh singh negi CALCULATOR")

##win.configure(width=500,height=500,background="yellow") ##method 1 to change size
win.geometry("300x125+0+0")##method 2 to change size +0+0 is x, y  where it appers

label=ttk.Label(win,text="hello world") ##.label() method makes a label

##order of things does not matter by arguments u create but matters by packing , see button comes first
button=ttk.Button(win,text="hello")##only tk also gives button but not that much smooth
##button.pack()
##label.pack()
##see that most of these objects start with tk.capital  ttk.capital
entry = ttk.Entry(win,justify="right",textvariable=text)##ACCEPTS SINGLE  line text string from the user, justify is an optional argument which starts the string from right
entry.grid(row=0, columnspan=4,sticky="nesw") ##used textvariable so that it can change after = clicked
button_7=ttk.Button(win,text="7",command=press(7))##idk why lambda is imp here , its not
button_7.grid(row=1, column=0)

button_8=ttk.Button(win,text="8",command=lambda:press(8))
button_8.grid(row=1, column=1)

button_9=ttk.Button(win,text="9",command=lambda:press(9))
button_9.grid(row=1, column=2)

button_d=ttk.Button(win,text="/",command=lambda:press("/"))
button_d.grid(row=1, column=3)


button_4=ttk.Button(win,text="4",command=lambda:press(4))
button_4.grid(row=2, column=0)

button_5=ttk.Button(win,text="5",command=lambda:press(5))
button_5.grid(row=2, column=1)

button_6=ttk.Button(win,text="6",command=lambda:press(6))
button_6.grid(row=2, column=2)

button_1=ttk.Button(win,text="1",command=lambda:press(1))
button_1.grid(row=3, column=0)

button_2=ttk.Button(win,text="2",command=lambda:press(2))
button_2.grid(row=3, column=1)

button_3=ttk.Button(win,text="3",command=lambda:press(3))
button_3.grid(row=3, column=2)

button_m=ttk.Button(win,text="*",command=lambda:press("*"))
button_m.grid(row=2, column=3)


button_p=ttk.Button(win,text="+",command=lambda:press("+"))
button_p.grid(row=3, column=3)

button_s=ttk.Button(win,text="-",command=lambda:press("-"))
button_s.grid(row=4, column=3)

button_0=ttk.Button(win,text="0",command=lambda:press(0))
button_0.grid(row=4, column=0)

button_de=ttk.Button(win,text=".",command=lambda:press("."))
button_de.grid(row=4, column=1)

button_c=ttk.Button(win,text="C",command=lambda:clr())
button_c.grid(row=4, column=2)

button_e=ttk.Button(win,text="=",command=lambda:equal())
button_e.grid(row=5, columnspan=4,sticky="nsew") ##columnspan says take up all 4 blocks in row 5 , sticky nsew says to expand in all directions

def clr():
    
    global expr
    expr=""
    text.set(expr)

def equal():
    global expr
    ttl=str(eval(expr))
    text.set(ttl)
    ##its like assigning expr to text
#if we make a button on a button already it overwrites it
##u do not need to pack if u use grid
##pack and grid do not use toghther

win.mainloop()
## "6"+"3" gives "63"
## "6+3" gives "6+3"
##eval("6+3") gives 9 python knows its also a integer , returns int

