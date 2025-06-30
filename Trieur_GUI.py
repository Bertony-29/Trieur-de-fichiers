import os
import shutil
import tkinter as tk
from tkinter import filedialog,messagebox,scrolledtext,ttk

def parcours():
    text.delete("1.0","end")
    dialog = filedialog.askdirectory()
    chemin.insert(0,dialog)

def ouvrir_dossier(dossier):
    reponse = messagebox.askyesno("Confirmation","Voulez-vous voir le dossier trié ?")
    if reponse:
        try :
            dossier1 = os.path.normpath(dossier)
            os.startfile(dossier1)
        except Exception as e :
            messagebox.showerror("Erreur",f"Impossible d'ouvrir le dossier {dossier}:{e}")    


def tri():
    text.delete("1.0","end")

    # Commençons par afficher l'extension de chaque fichier
    Dossier_a_trier = chemin.get()
    try :
        fichiers = os.listdir(Dossier_a_trier)
        print(fichiers)
    except FileNotFoundError as e:
        messagebox.showerror("Dossier introuvable !",f"Le dossier {Dossier_a_trier} est introuvable")
        return
    for fichier in fichiers:
        route = os.path.join(Dossier_a_trier,fichier)
        if os.path.isfile(route):
            nom, extension = os.path.splitext(fichier)
            print(f"{fichier}, extension : {extension}")

            # Ignorer les fichiers sans extensions
            if extension == "":
                continue

            Dossier_cible = os.path.join(Dossier_a_trier,extension.lstrip("."))

            try :
                os.makedirs(Dossier_cible, exist_ok=True)
            except OSError as o :
                messagebox.showerror("Erreur !",f"Erreur lors de la création du dossier {Dossier_cible} : {o}")

            source = os.path.join(Dossier_a_trier,fichier)
            destination = os.path.join(Dossier_cible,fichier)
            
            try :
                shutil.move(source,destination)
                text.insert("end",f"{fichier} à été déplacé.\n")
            except shutil.Error as s :
                messagebox.showerror("Erreur !",f"Erreur lors du déplacement de {fichier} : {s}")       
        
    print(os.listdir(Dossier_a_trier))
    messagebox.showinfo("Fin du tri","Le tri est terminé.")
    ouvrir_dossier(Dossier_a_trier)
    chemin.delete(0,tk.END)
     
    

# créer une première fenêtre et configurer ses paramètres
root = tk.Tk()
root.title("Trieur de fichiers")
root.geometry("700x600")
root.configure(bg="darkblue")
root.grid_columnconfigure(0,weight=1)
#styles

style = ttk.Style()
style.theme_use("clam")
style.configure("Bouton.TButton",foreground="black", background="grey")
style.configure("Main.TLabel",foreground="black", background="darkblue", font=("Arial", 12, "bold underline"))
style.configure("Frame.TFrame", background="grey")
style.configure("Label1.TLabel",font = ("Arial",24, "bold underline"),background ="darkblue")
style.configure("label.TLabel",background="grey",font=("Arial",12,"underline"))


#Ajout d'un titre
titre = ttk.Label(root, text="Trieur de fichiers",style="Label1.TLabel")
titre.grid(row=0,column=0, pady=50)

#Conteneur permettant d'ajouter des éléments
frm = ttk.Frame(root,style="Frame.TFrame")
frm.grid(row=1,column=0,padx=50,pady=10)

#Ajout d'un suivi du dossier trié
text = scrolledtext.ScrolledText(root,width=50,height=10)
text.grid(row=2,column=0, padx=5,pady=30)

#Ajouter un pied de page
piedDePage = ttk.Label(root,text="Développé par Bertony © 2025",style="Main.TLabel")
piedDePage.grid(row=3, column=0, pady=20)

# Dans le conteneur :

# ajout d'un champ de saisie 
label = ttk.Label(frm, text="Dossier :",style ="label.TLabel")
label.grid(row=0, column=0, padx=5, pady=5)
chemin = ttk.Entry(frm,width=40)
chemin.grid(row=0, column=1, padx=5, pady=5,sticky="ew")

#ajout d'un bouton de parcours
Parcours = ttk.Button(frm, text= "Parcourir",command=parcours,style="Bouton.TButton")
Parcours.grid(row=0, column=2, padx=5, pady=5)

#ajout d'un bouton de tri
Tri = ttk.Button(frm, text= "Trier le dossier",command=tri,style="Bouton.TButton")
Tri.grid(row=1, column=0, columnspan=3, padx=5, pady=10)



#afficher la fenêtre
root.mainloop()




