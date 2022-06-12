import opendatasets 
import os


def load_kaggle_data(dataset_path, local_dir="../data/raw/"):
    opendatasets.download(dataset_path, data_dir=local_dir)
    dir_name = dataset_path.split('/')[-1]
    local_path = "../data/raw/"+dir_name
    return local_path, os.listdir(local_path)