#import all required package
import os
import numpy as np
import sys
import dill
import yaml

from src.forest.exception import ForestException
from src.forest.logger import logging



#Read yaml file
def read_yaml_file(file_path:str)-> dict:       #->dict (return type)
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)    #return text to dict
    except Exception as e:
        raise ForestException(e,sys) from e


#write yaml file                  
def write_yaml_file(file_path:str,content: object,replace: bool = False)->None: #Write, so return not required
    """file_path = str(file type) 
    Content: dict_file   
    replace: (default) false"""
    try:
        if replace:   #To ensure file path present or not
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(file_path,exist_ok=True)

        with open(file_path,"w") as file:
            yaml.dump(content,file)        
    except Exception as e:
        raise ForestException(e,sys) from e
    

#load object(or, load pickel file)
def load_object(file_path:str)-> object:
    """Load pre-saved object
       return type python object(dict/model/etc)"""
    
    logging.info("Entered the load_object method of main_utils class")
    try:
        with open(file_path,"rb") as file_obj:                      #rb: read binary
            obj = dill.load(file_obj)
        logging.info("Exit the load_object method of main_utils class")
        return obj
    except Exception as e:
        raise ForestException(e,sys) from e
    

#save object(or, load pickel file)
def save_object(file_path:str,content:object)->None:
    """Save Object"""
    logging.info("Entered the save_object method of main_utils class")
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:                      #wb: write binary
            dill.dump(obj=object,file=file_obj)

        logging.info("Exit the save_object method of main_utils class")

    except Exception as e:
        raise ForestException(e,sys) from e
    

#Save numpay array data
def save_numpy_array_data(file_path: str,array: np.array):
    """Save numpy array to a file in a binary format"""
    try:
        dir_path = os.path.dirname(file_path)  #remove .xyz
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise ForestException(e,sys) from e

#load numpay array data
def load_numpy_array_data(file_path: str)-> np.array:
    """load the numpy array data"""
    try:
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise ForestException(e,sys) from e


#Create directory
def create_directory(path_to_directories: list,verbose:True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"Create directory at: {path}")