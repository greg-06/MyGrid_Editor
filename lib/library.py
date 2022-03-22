from cgitb import text
import os
from tkinter import filedialog, Tk, Menu
from turtle import undo

savedFile = {1: ""}


class grilleEditor:
    def __init__(self, main_window, zone_edition):
        self.main_window = main_window
        self.zone_edition = zone_edition

    # création de la fenêtre

    def create(self):
        '''création de la fenêtre'''
        self.main_window = Tk()
        self.main_window.title("MyGrid")
        self.main_window.geometry("700x400")

    def add_Text(self):
        '''création de la zone de texte'''
        self.zone_edition = text(self.main_window, undo=True)
        self.zone_edition.pack(expand=True, fill='both')

    def generate(self):
        '''génération de la fenêtre'''
        self.main_window.mainloop()

    # Création du menu

    def nouvelleGrille(self):
        # ACTIONS DU MENU FICHIER
        os.popen("python main.py")

    def ouvrir(self):
        file = filedialog.askopenfilename(initialdir="/", title="sélectionner le fichier", filetype=(("Text File", "*.txt"), ("All Files", "*.*")))
        f = open(file, 'r')
        app = f.read()
        f.close()
        self.zone_edition.insert("1.0", "r")

    def enregistrer_sous(self):
        fichier = filedialog.asksaveasfilename(defaultextension=".*", initialdir="/", title="Enregistrer Sous", filetype=(("Texte File", "*.txt"), ("xls file", "*.xls"), ("All File", "*.*")))
        savedFile[1] = fichier
        f = open(fichier, 'w')
        s = self.zone_edition.get("1.0", END)
        f.write(s)
        f.close()

    def savegarder(self):
        if (savedFile[1] == ""):
            saved.enregistrer_sous()
        else:
            f = open(savedFile[1], 'w')
            s = self.zone_edition.get("1.0", END)
            f.write(s)
            f.close()

    def quitter(self):
        self.main_window.quit()

    def annuler(self):
        self.zone_edition.edit_undo()

    def retablir(self):
        self.zone_edition.edit_redo()

    def copier(self):
        self.zone_edition.clipboard_clear()
        self.zone_edition.clipboard_append(self.zone_edition.selection.get())

    def couper(self):
        self.copier()
        self.zone_edition.delete('sel.first', 'sel.last')

    def coller(self):
        self.zone_edition.insert(insert, self.zone_edition.clipboard_get)

    def info(self):
        print("Bonjour !")

    # ETIQUETTES DES MENUS

    def add_menu(self):
        menuBar = Menu(self.main_window)

        # Menu Fichier

        menuFichier = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Fichier", menu=menuFichier)
        menuFichier.add_command(label="Créer une nouvelle grille", command=self.nouvelleGrille)
        menuFichier.add_command(label="Ouvrir", command=self.ouvrir)
        menuFichier.add_command(label="Enregistrer Sous", command=self.enregistrer_sous)
        menuFichier.add_command(label="Sauvegarder", command=self.savegarder)
        menuFichier.add_command(label="Quitter", command=self.quitter)

        # Menu édition

        menuEdition = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Edition", menu=menuEdition)
        menuEdition.add_command(label="Annuler", command=self.annuler)
        menuEdition.add_command(label="Rétablir", command=self.retablir)
        menuEdition.add_command(label="Copier", command=self.copier)
        menuEdition.add_command(label="Couper", command=self.couper)
        menuEdition.add_command(label="Coller", command=self.coller)

        # Menu Aide

        menuAide = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Aide", menu=menuAide)
        menuAide.add_command(label="A propos", command=self.info)

        self.main_window.config(menu=menuBar)
