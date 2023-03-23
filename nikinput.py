from tkinter import *
import config
import os

class main:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tk = Tk()
        self.tk['bg'] = config.NMAINBG
        
    def getName():
        return open(config.NFILENAME, 'r').readline()
    
    def writeName(self, nik:str = ''):
        if nik == '':
            nik = "Nikita gay"
        with open(config.NFILENAME, 'w') as n:
            n.write(nik)
            n.close()

    def setname(self, x:int = None, y:int = None):
        if not x:
            x = self.x
        if not y:
            y = self.y
        self.tk.geometry(str(x)+'x'+str(y))
        self.tk.title('enter your nikname')

        nameField = Entry(self.tk,font=('Arial',15), bg=config.NINPUTBG, fg=config.NINPUTFG, width=25)
        sumbitButton = Button(
            self.tk,
            cursor='circle',
            text="Enter", 
            bg=config.NBUTTONBG,
            font=("Arial", 12),
            border=0,
            width=20,
            fg=config.NBUTTONFG,
            command=lambda:self.writeName(nameField.get()[:config.NMAXLEN]))
        
        nameField.pack(side=TOP)
        sumbitButton.pack(side=TOP)
        self.tk.mainloop()

main(512, 512).setname()
