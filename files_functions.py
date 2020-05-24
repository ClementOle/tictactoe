import pickle

import data

file_name = 'save.data'


def get_file_dict():
    """Open the save file and return the value"""
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except:
        return {}


def init_wall_of_fame():
    """Init the dictionary with the data from the save file"""
    data.wall_of_fame = get_file_dict()


def write_dict_in_file(dict):
    """Write the dictionary in the save file"""
    try:
        with open(file_name, 'wb+') as file:
            pickle.dump(dict, file)
    except:
        return
