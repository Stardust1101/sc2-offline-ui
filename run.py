import pip._internal as pipmain
from time import *

import sc2

import tkinter as tk
import os

from sc2 import Race, Difficulty
from sc2.player import Human, Computer

#  Star Craft 2 directory
file = open('C:\\Users\\15650\\Documents\\StarCraft II\\ExecuteInfo.txt')
dir = file.read()
file.close()
dir = dir.split(' = ')[1]; ind = dir.find('\Versions')
dir = dir[:ind]
map_l = os.listdir(dir + '\Maps')
race = [
    'Protoss',
    'Terran',
    'Zerg',
    'Random'
]

window = tk.Tk()
window.title = ('Starcraft II')
window.geometry('420x480')
l = tk.Label(window, text='Maps', height=2, width=20)
l.grid(row=0, column=0, padx=20)
lb = tk.Listbox(window, height=20, width=20, exportselection=0)
for m in map_l:
    lb.insert('end', m[0:-7])
lb.grid(row=1, column=0, rowspan=5, padx=20)

#  Player Race
l2 = tk.Label(window, text='Race', height=2, width=20)
l2.grid(row=0, column=1, padx=20)
lb2 = tk.Listbox(window, height=5, width=20, exportselection=0)
for r in race:
    lb2.insert('end', r)
lb2.grid(row=1, column=1, padx=20)

#  Computer Race
l3 = tk.Label(window, text='Opponent Race', height=2, width=20)
l3.grid(row=2, column=1, padx=20)
lb3 = tk.Listbox(window, height=5, width=20, exportselection=0)
for r in race:
    lb3.insert('end', r)
lb3.grid(row=3, column=1, padx=20)

#  Difficulty
Dif = [
    'VeryEasy',
    'Easy',
    'Medium',
    'MediumHard',
    'Hard',
    'Harder',
    'VeryHard',
    'CheatVision',
    'CheatMoney',
    'CheatInsane'
]
l4 = tk.Label(window, text='Difficulty', height=2, width=20)
l4.grid(row=4, column=1, padx=20)
def print_selection(s):
    l4.config(text=Dif[int(s)])
s = tk.Scale(window, label='Difficulty', from_=0, to=9, orient=tk.HORIZONTAL,
             length=150, tickinterval=3, resolution=1, command=print_selection, width=25)
s.grid(row=5, column=1, padx=20)

#  Save Replay
v = tk.IntVar()
c = tk.Checkbutton(window, text='Replay?', variable=v, onvalue=1, offvalue=0)
c.grid(row=6, column=1, padx=20)

#  Start
def get_info():
    map_s = lb.get(tk.ACTIVE)
    rc = lb2.get(tk.ACTIVE)
    op_r = lb3.get(tk.ACTIVE)
    dif = Dif[s.get()]
    rep = v.get()
    if rep == 1:
        r1 = str(time()) + rc[0] + op_r[0] + map_s + '.SC2Replay'
    else:
        r1 = None

    Dicx = {
        'Terran': Race.Terran,
        'Protoss': Race.Protoss,
        'Zerg': Race.Zerg,
        'Random': Race.Random,
        'VeryEasy': Difficulty.VeryEasy,
        'Easy': Difficulty.Easy,
        'Medium': Difficulty.Medium,
        'MediumHard': Difficulty.MediumHard,
        'Hard': Difficulty.Hard,
        'Harder': Difficulty.Harder,
        'VeryHard': Difficulty.VeryHard,
        'CheatVision': Difficulty.CheatVision,
        'CheatMoney': Difficulty.CheatMoney,
        'CheatInsane': Difficulty.CheatInsane
    }

    sc2.run_game(
        sc2.maps.get(map_s),
        [
            Human(Dicx[rc], fullscreen=True),
            Computer(Dicx[op_r], Dicx[dif]),  # CheatInsane VeryHard
        ],
        realtime=True,
        save_replay_as=r1
    )

b = tk.Button(window, text='Start', width=18, height=1, command=get_info)
b.grid(row=6, column=0, padx=20, pady=20)

window.mainloop()



