import tkinter as tk
from tkinter import filedialog, messagebox
from backup import BackupManager
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def start_backup():
    source = filedialog.askdirectory(title="Choisir le dossier source")
    destination = filedialog.askdirectory(title="Choisir le dossier de destination")

    if not source or not destination:
        return

    compress = compress_var.get()
    manager = BackupManager(source, destination, zip_enabled=compress)
    result = manager.copy_folder()

    # Sauvegarde dans le fichier config
    save_config({"last_source": source, "last_destination": destination})
    messagebox.showinfo("Sauvegarde", f"Sauvegarde terminée :\n{result}")

# Interface graphique
root = tk.Tk()
root.title("Backup Manager")
root.geometry("400x200")

config = load_config()

tk.Label(root, text="Gestionnaire de Sauvegarde", font=("Arial", 14)).pack(pady=10)

compress_var = tk.BooleanVar()
compress_checkbox = tk.Checkbutton(root, text="Compresser (ZIP)", variable=compress_var)
compress_checkbox.pack(pady=5)

backup_button = tk.Button(root, text="Démarrer la sauvegarde", command=start_backup)
backup_button.pack(pady=20)

root.mainloop()
