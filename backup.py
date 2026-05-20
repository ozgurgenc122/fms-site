import os
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

backup_root = os.path.join(BASE_DIR, "yedekler")

if not os.path.exists(backup_root):
    os.makedirs(backup_root)

tarih = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

backup_folder = os.path.join(backup_root, f"yedek_{tarih}")

os.makedirs(backup_folder)

dosyalar = [
    "db.sqlite3",
]

klasorler = [
    "media",
    "templates",
    "takip",
]

for dosya in dosyalar:
    kaynak = os.path.join(BASE_DIR, dosya)

    if os.path.exists(kaynak):
        shutil.copy2(kaynak, backup_folder)

for klasor in klasorler:
    kaynak = os.path.join(BASE_DIR, klasor)

    if os.path.exists(kaynak):
        hedef = os.path.join(backup_folder, klasor)

        shutil.copytree(kaynak, hedef)

print(f"\nYEDEK ALINDI:\n{backup_folder}")