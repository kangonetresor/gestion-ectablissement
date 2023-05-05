 from tkinter import *
import mysql.connector 
from PIL import ImageTk, Image

class Accueil:
    def __init__(self, root):

        self.root = root
        self.root.title("Page d'accueil")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="white")

        # img = Image.open("univ_bat.jpg")
        # img = img.resize((1920,1080), resample=Image.LANCZOS)
        # bg_img = ImageTk.PhotoImage(img)
        # bg_img = PhotoImage(img)
        # bg_label = Label(self.root, image=bg_img)

        # bg_label.image = bg_img
        # bg_label.place(x=0,y=0, relwidth=1, relheight=1)

        entete = Frame(self.root, bg="cyan", bd=5, relief="sunken")
        entete.place(x=10, y=5, width=1505, height=100)

        #Tableau de bord
        premiermot = Label(self.root, text = "Tableau de bord", font=("new time roman", 30))
        premiermot.place(x=150,y=200)



root = Tk()
objet = Accueil(root)
root.mainloop()
