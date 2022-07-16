from tkinter import *

class Checkbar(Frame):
    def __init__(self, parent=None, picks={}, side=LEFT, anchor=W, list_keys=[]):
        Frame.__init__(self, parent)
        self.vars = []
        maxwidth = len(max(list_keys, key=len))

        for key, value in picks.items():
            var = IntVar()
            chk = Checkbutton(self, text=key, variable=var, width=maxwidth, anchor='w')
            # button_ttp = ToolTip(chk, value)
            chk.pack(side=side, anchor=anchor, expand=YES, )



root = Tk()
list_keys = ['1', '2', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']

Label(root, text='Select keyword(s):').grid(row=0, column=0)
Checkbar(root, picks={k: k for k in list_keys[:4]}, list_keys=list_keys).grid(row=0, column=1, sticky='w')
Checkbar(root, picks={k: k for k in list_keys[4:]}, list_keys=list_keys).grid(row=1, column=1, sticky='w')
root.mainloop()