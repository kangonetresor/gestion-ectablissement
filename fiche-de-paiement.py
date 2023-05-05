# l'outil pack pour le placement du widget en lui meme
# Exemple de creation de boutton :  btn = Button(root, text="Carré\naléatoire", command=dessiner)



####################################### 
# code pour ouvrir plusieurs fenetres #
#Cela va afficher la fenetre maitresse#
# et pour la cacher on fair           #
# root.withdraw() avant mainloop      #
#                                     #
# from tkinter import *               #
# root = Tk()                         #
# a = Toplevel(root, bg=’red’)        #
# b = Toplevel(root, bg=’blue’)       #
# root.mainloop()                     #
#######################################






from tkinter import *

class Outils:
    def __init__(self, root):
        # tout ce qui concerne la fenetre en elle meme
        self.root = root
        self.root.title("Fiche d'inscription d'eleves") # Pour donner un titre a notre fenetre 
        self.root.config(bg="lightblue") # configuration de la couleur #autre couleur ivory
        self.root.resizable(False, False) # Permet le redimenssionement par l'utilisateur
        self.root.geometry("900x700+300+1") #on gere l'affichage geometrique de notre fenetre  
        self.root.labelprincipale = Label(root, text="ENREGISTRER LE PAIEMENT D'UN ELEVE", bg="lightblue", font=("Cyan", 15, "bold")) # Premier titre
        self.root.labelprincipale.place(x=0,y=1) #placement du labelprincipale

        #Pour importer une photo
        #logo = PhotoImage(file="search.png")

        #
        self.root.entreerecherhce = Entry(root).place(x=650,y=70)
        self.root.boutrecherche = Button(root, text="Ok", width=5, height=2).place(x=780, y=70)
        self.root.mot = Label(root, text="Rechercher un eleve \n (avec Matricule)", bg="lightblue", font=("Times", 10, "bold")).place(x=650,y=90)
        #Image a placer en bouton
        #  self.root.boutrecherche = Button(root, image=logo).place(x=780, y=70)

        # self.root.boutrecherche = Button(root, width=50, height=50, image=logoresearch).place(x=700, y=70)

        # Label Matricule
        self.root.matricule = Label(root, text="Matricule :", bg="lightblue", font=("Times", 15))
        self.root.matricule.place(x=100,y=150)
        self.root.entreerecherhce = Entry(root, width=70).place(x=280,y=150) # Pour placer les entrer de texte

        #
        self.root.montantpaye = Label(root, text="Montant paye :", bg="lightblue", font=("Times", 15)).place(x=100,y=200)
        self.root.entreerecherhce = Entry(root, width=70).place(x=280,y=200)

        #
        self.root.resteapaye = Label(root, text="Reste a paye :", bg="lightblue", font=("Times", 15)).place(x=100,y=250)
        self.root.entreerecherhce = Entry(root, width=70).place(x=280,y=250)

        #
        self.root.datepaiement = Label(root, text="Date de paiement :", bg="lightblue", font=("Times", 15)).place(x=100,y=300)
        self.root.entreerecherhce = Entry(root, width=70).place(x=280,y=300)

        #
        self.root.modepaiement = Label(root, text="Mode de paiement :", bg="lightblue", font=("Times", 15)).place(x=100,y=350)
        



root = Tk()  # Tk est un constructeur (permet la ceation d'une fenetre maitraisse)
objet = Outils(root) #instantiation de la class outils en l'appelant 

root.mainloop() #lancement de l'application graphique