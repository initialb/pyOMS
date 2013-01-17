# -*- coding: utf-8 -*-
import Tkinter
def on_click():
    label['text'] = text.get()
root = Tkinter.Tk(className='bitunion')
label = Tkinter.Label(root)
label['text'] = 'be on your own'
label.pack()
text = Tkinter.StringVar()
text.set('change to what?')
entry = Tkinter.Entry(root)
entry['textvariable'] = text
entry.pack()
button = Tkinter.Button(root)
button['text'] = 'change it'
button['command'] = on_click
button.pack()
root.mainloop()
