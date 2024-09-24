import os
import shutil
from pathlib import Path

def organize_files(directory):
    # Définir les extensions pour chaque catégorie
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Musique': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z']
    }

    # Parcourir tous les fichiers dans le répertoire
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Ignorer les dossiers
        if os.path.isfile(file_path):
            # Obtenir l'extension du fichier
            file_extension = Path(filename).suffix.lower()
            
            # Trouver la catégorie correspondante
            for category, extensions in categories.items():
                if file_extension in extensions:
                    # Créer le dossier de catégorie s'il n'existe pas
                    category_path = os.path.join(directory, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    
                    # Déplacer le fichier
                    shutil.move(file_path, os.path.join(category_path, filename))
                    print(f"Déplacé {filename} vers {category}")
                    break
            else:
                # Si aucune catégorie ne correspond, mettre dans "Autres"
                other_path = os.path.join(directory, "Autres")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                shutil.move(file_path, os.path.join(other_path, filename))
                print(f"Déplacé {filename} vers Autres")

# Utilisation du script
if __name__ == "__main__":
    directory = input("Entrez le chemin du dossier à organiser : ")
    organize_files(directory)
    print("Organisation terminée !")
