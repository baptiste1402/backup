# Backup Manager

Projet Python de gestion de sauvegarde de fichiers et de répertoires avec interface graphique, gestion des versions, compression ZIP, journalisation des opérations, et configuration utilisateur.

---

## Objectif

Créer un programme de sauvegarde robuste permettant à l'utilisateur de :

- Sélectionner un dossier source et un dossier de destination
- Sauvegarder tous les fichiers et sous-dossiers
- Générer des versions horodatées (avec ou sans compression ZIP)
- Enregistrer un journal des opérations
- Conserver les chemins récents utilisés grâce à un fichier de configuration
- Interagir via une **interface graphique (Tkinter)** simple et intuitive
  
## Technologies utilisées

- **Python 3.9+**
- `tkinter` (interface graphique)
- `shutil`, `os`, `zipfile` (système de fichiers)
- `json` (configuration)
- `logging` (fichier journal)
- `datetime` (horodatage)
  
## Instructions d'installation et d'exécution

- Cliquez sur le bouton “Démarrer la sauvegarde”
- Une fenêtre s’ouvre pour sélectionner le dossier source à sauvegarder
- Une deuxième fenêtre s’ouvre pour sélectionner le dossier de destination
- (Optionnel) Cochez la case “Compresser (ZIP)” pour créer une archive .zip au lieu d’un dossier classique
- Attendez quelques secondes que la sauvegarde s’effectue
- Un message s’affiche pour confirmer la réussite et afficher le nom de la sauvegarde créée


