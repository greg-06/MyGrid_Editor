from tkinter import * 
import os

from lib.library import *

r = Tk().withdraw()
c = Text(r)

root = grilleEditor(r, c)

root.create()
root.add_Text()
root.add_menu()
root.generate()
