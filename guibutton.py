from tkinter import*
root = Tk()
def myClick():
 myLabel = Label(root,text = "you have clicked a button")


myButton = Button(root,text="click me",command = myClick,fg = "blue",bg = "red")
                  
myButton.pack()
root.mainloop()