from tkinter import *
import config
from os import system
import threading
import helplib as hl

class main:
    def __init__(self, xscale, yscale):
        self.xs = xscale
        self.ys = yscale
        self.tk = Tk()
        self.tk.configure(background=config.MMAINBG)
        self.tk.geometry(str(xscale)+'x'+str(yscale))
        self.tk.title('Main menu')

    
    def get(self):
        try:
            threading.Thread(target=print(''))
        except:
            print('please, launch menu in special thread')
        PlayButton = Button(
            self.tk,
            text='Play',
            width=21,
            bg=config.MBUTTONBG,
            fg=config.MBUTTONFG,
            command=lambda:hl.runFile(config.GAMEFILENAME)
            ).place(x=self.xs//2,y=self.ys//2-30,anchor='center')

        SettingsButton = Button(
            self.tk,
            text='settings',
            width=25,
            bg=config.MBUTTONBG,
            fg=config.MBUTTONFG,
            command=lambda:hl.runFile(config.CONFIGFILENAME, 'notepad.exe')
            ).place(x=self.xs//2,y=self.ys//2,anchor='center')

        ExitButton = Button(
            self.tk,
            text='Quit',
            width=20,
            bg=config.MBUTTONBG,
            fg=config.MBUTTONFG,
            command=lambda:self.tk.quit()
            ).place(x=self.xs//2,y=self.ys//2+30,anchor='center')
        self.tk.mainloop()

main(500, 400).get()
