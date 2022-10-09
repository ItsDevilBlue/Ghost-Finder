from tkinter import *
import os
ghosts = {'banshee': ['dots', 'fingerprints', 'orbs'], 'demon': ['fingerprints', 'freezing', 'writing'], 'deogen': ['dots', 'spirit box', 'writing'], 'goryo': ['dots', 'emf', 'fingerprints'], 'hantu': ['fingerprints', 'freezing', 'orbs'], 'jinn': ['emf', 'fingerprints', 'freezing'], 'mare': ['orbs', 'spirit box', 'writing'], 'mimic': ['fingerprints', 'freezing', 'orbs', 'spirit box'], 'moroi': ['freezing', 'spirit box', 'writing'], 'myling': ['emf', 'fingerprints', 'writing'], 'obake': ['emf', 'fingerprints', 'orbs'], 'oni': ['dots', 'emf', 'freezing'], 'onryo': ['freezing', 'orbs' ,'spirit box'], 'phantom': ['dots', 'fingerprints', 'spirit box'], 'poltergeist': ['fingerprints', 'spirit box', 'writing'], 'raiju': ['dots', 'emf', 'orbs'], 'revenant': ['freezing', 'orbs', 'writing'], 'shade': ['emf', 'freezing', 'writing'], 'spirit': ['emf', 'spirit box', 'writing'], 'thaye': ['dots', 'orbs', 'writing'], 'twins': ['emf', 'freezing', 'spirit box'], 'wraith': ['dots', 'emf', 'spirit box'], 'yokai': ['dots', 'orbs', 'spirit box'], 'yurei': ['dots', 'freezing', 'orbs']}
user_evidence = []

def add_dots():
    global user_evidence
    user_evidence.append('dots')
    dots_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    dots_btn.config(state=DISABLED)

def add_writing():
    global user_evidence
    user_evidence.append('writing')
    writing_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    writing_btn.config(state=DISABLED)

def add_freezing():
    global user_evidence
    user_evidence.append('freezing')
    freezing_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    freezing_btn.config(state=DISABLED)

def add_orbs():
    global user_evidence
    user_evidence.append('orbs')
    orbs_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    orbs_btn.config(state=DISABLED)

def add_emf():
    global user_evidence
    user_evidence.append('emf')
    emf_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    emf_btn.config(state=DISABLED)

def add_spirit():
    global user_evidence
    user_evidence.append('spirit box')
    spirit_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    spirit_btn.config(state=DISABLED)

def add_prints():
    global user_evidence
    user_evidence.append('fingerprints')
    prints_btn.config(fg='lime', disabledforeground='lime')

    if len(user_evidence) > 2:
        find_btn.config(state=NORMAL)
    prints_btn.config(state=DISABLED)

def open_docs():
    os.startfile(f'docs\{user_ghost}.txt')

def find_ghosts():
    global user_evidence, ghosts, user_ghost

    user_evidence = sorted(user_evidence)
    
    for ghost in ghosts:
        if user_evidence == ghosts[ghost]:
            user_ghost = ghost
            win = Tk()
            win.title('Ghost')
            win.config(bg='gray')
            win.attributes('-toolwindow', True)
            win.resizable(0, 0)
            win.geometry('120x120')

            ghost_label = Label(win, bg='gray', text=f'Your ghost is a... \n{user_ghost.upper()}', font=('bold', 12))
            ghost_label.pack()

            open_btn = Button(win, text='Open Docs', command=open_docs, width=10, height=2, borderwidth=1)
            open_btn.pack(pady=20)
    clear()
    
def clear():
    global user_evidence
    user_evidence.clear()
    dots_btn.config(fg='black', state=NORMAL)
    emf_btn.config(fg='black', state=NORMAL)
    writing_btn.config(fg='black', state=NORMAL)
    freezing_btn.config(fg='black', state=NORMAL)
    orbs_btn.config(fg='black', state=NORMAL)
    spirit_btn.config(fg='black', state=NORMAL)
    prints_btn.config(fg='black', state=NORMAL)
    find_btn.config(state=DISABLED)

root = Tk()

root.title('Ghost Finder')
root.config(bg='gray')
root.geometry('250x250')
root.iconbitmap('icon\gf_icon.ico')
root.resizable(0, 0)

dots_btn = Button(root, text='D.O.T.S', command=add_dots, width=7, height=2, borderwidth=1)
dots_btn.place(x=10, y=10)

writing_btn = Button(root, text='Ghost Writing', command=add_writing, height=2, borderwidth=1)
writing_btn.place(x=80, y=10)

emf_btn = Button(root, text='EMF 5', command=add_emf, width=7, height=2, borderwidth=1)
emf_btn.place(x=175, y=10)

freezing_btn = Button(root, text='Freezing', command=add_freezing, width=7, height=2, borderwidth=1)
freezing_btn.place(x=10, y=60)

orbs_btn = Button(root, text='Ghost Orbs', command=add_orbs, width=10, height=2, borderwidth=1)
orbs_btn.place(x=82, y=60)

spirit_btn = Button(root, text='Spirit Box', command=add_spirit, width=7, height=2, borderwidth=1)
spirit_btn.place(x=175, y=60)

prints_btn = Button(root, text='Fingerprints', command=add_prints, width=10, height=2, borderwidth=1)
prints_btn.place(x=82, y=110)

line_label = Label(root, text='----------------------------------------------------', bg='gray')
line_label.place(x=1, y=150)

find_btn = Button(root, text='Find Ghost', command=find_ghosts, width=10, height=2, borderwidth=1)
find_btn.place(x=25, y=180)
find_btn.config(state=DISABLED)

clear_btn = Button(root, text='Clear', fg='red', command=clear, width=10, height=2, borderwidth=1)
clear_btn.place(x=150, y=180)

root.mainloop()
