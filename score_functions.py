import data


def sort_dict(dict):
    """ Sort the dictionary from largest to smallest """
    return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def print_wall_of_fame():
    """ Print the wall of fame """
    sorted_dict = sort_dict(data.wall_of_fame)
    for index, keys in enumerate(sorted_dict):
        print("{0} - {1} -- {2}".format(index + 1, keys, sorted_dict[keys]))
