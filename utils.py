import os
import shutil
import kagglehub
from config import DATA_PATH

def ingest_kaggle_database(path):
    #1. Retrieve the download path
    download_path = kagglehub.dataset_download(path)
    
    #2. Access the database file name
    downloaded_files = os.listdir(download_path) #Lists downloaded files
    sqlite_file = next(f for f in downloaded_files if f.endswith(".sqlite")) #Gets the first .sqlite file
    
    #3. Create the full file path (.sqlite file alone insufficient for access)
    full_path = os.path.join(download_path, sqlite_file)
    
    #4. Create data folder for the path to go in
    os.makedirs(DATA_PATH, exist_ok = True)
    
    #5. Move full file path into the folder
    shutil.copy(full_path, DATA_PATH)