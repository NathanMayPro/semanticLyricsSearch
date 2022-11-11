import os 
import sys

from utils.env import *

if __name__ =="__main__":
    """ The goal is to download all files from data source and save them to local disk"""
    DATA_SOURCE_FILE = "data_source.txt"
    DATA_DEST_DIR = "./data/data_lake/data_source_txt/"
    
    # ensure data source dir exist
    if ensure_path(DATA_DEST_DIR):
        # clean all precedent files
        clean_path(DATA_DEST_DIR, keep_dir = True)
        # for each file in data source, download it
        data_source_url_list = extract_data(DATA_SOURCE_FILE, remove_element = "\n")
        for url in data_source_url_list:
            file_name = url_to_file_name(url)
            download_file(url, os.path.join(DATA_DEST_DIR, file_name))
    pass