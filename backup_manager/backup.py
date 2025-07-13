import os
import shutil
import zipfile
import logging
from datetime import datetime

class BackupManager:
    def __init__(self, source, destination, zip_enabled=False):
        self.source = source
        self.destination = destination
        self.zip_enabled = zip_enabled
        self.setup_logging()

    def setup_logging(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        logging.basicConfig(
            filename="logs/backup.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def create_backup_folder(self):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder_name = f"backup_{now}"
        full_path = os.path.join(self.destination, folder_name)
        os.makedirs(full_path, exist_ok=True)
        return full_path

    def copy_folder(self):
        if not os.path.exists(self.source):
            error_msg = f"Le dossier source n'existe pas : {self.source}"
            logging.error(error_msg)
            return error_msg

        try:
            start_time = datetime.now()
            backup_folder = self.create_backup_folder()
            destination_path = os.path.join(backup_folder, os.path.basename(self.source))
            shutil.copytree(self.source, destination_path)
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()

            file_count = sum(len(files) for _, _, files in os.walk(destination_path))

            if self.zip_enabled:
                zip_path = self.compress_backup(backup_folder)
                logging.info(f"Backup compressé : {zip_path} ({file_count} fichiers, {duration:.2f}s)")
                return zip_path
            else:
                logging.info(f"Backup terminé : {destination_path} ({file_count} fichiers, {duration:.2f}s)")
                return destination_path

        except Exception as e:
            logging.error(f"Erreur lors de la sauvegarde : {str(e)}")
            return str(e)

    def compress_backup(self, folder_path):
        zip_path = folder_path + ".zip"
        shutil.make_archive(folder_path, 'zip', folder_path)
        shutil.rmtree(folder_path)  # Nettoyage du dossier temporaire
        return zip_path
