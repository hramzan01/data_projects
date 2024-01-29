import os as os
import shutil as sh
from datetime import datetime


def batch_rename(prefix, suffix, replace, replace_with):
    # get list of files in directory

    file_list = [file for file in os.listdir() if file if file != 'file_renamer.py' ]
    for file in file_list:
        base_name, extension = os.path.splitext(file)
        
        # replace words
        base_name = base_name.replace(replace,replace_with)
        
        # add prefix/suffix
        new_name = f'{prefix}{base_name}{suffix}{extension}'
       
        # rename files 
        os.rename(os.path.join(file),os.path.join(new_name))

    return
