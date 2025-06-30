 # créer un script python permettant de trier des dossiers

import os
import shutil


# Commençons par afficher l'extension de chaque fichier
Dossier_a_trier = ''
dossier1 = os.path.normpath(Dossier_a_trier)
os.startfile(dossier1)

try :
    fichiers = os.listdir(Dossier_a_trier)
except FileNotFoundError as e:
    print(f"Le dossier {Dossier_a_trier} est introuvable : {e}")
    exit(1)

for fichier in fichiers:
    chemin = os.path.join(Dossier_a_trier,fichier)
    if os.path.isfile(chemin):
        nom, extension = os.path.splitext(fichier)
        print(f"{fichier}, extension : {extension}")

        # Ignorer les fichiers sans extensions
        if extension == "":
            continue

        Dossier_cible = os.path.join(Dossier_a_trier,extension)

        try :
            os.makedirs(Dossier_cible, exist_ok=True)
        except OSError as o :
            print(f"Erreur lors de la création du dossier {Dossier_cible} : {o}")

        source = os.path.join(Dossier_a_trier,fichier)
        destination = os.path.join(Dossier_cible,fichier)
        
        try :
            shutil.move(source,destination)
        except shutil.Error as s :
            print(f"Erreur lors du déplacement de {fichier} : {s}")       


print(os.listdir(Dossier_a_trier))      
  

