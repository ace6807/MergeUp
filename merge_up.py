import os
import sys


def merge_up(master_folder):
    sub_dirs = os.listdir(master_folder)
    if len(sub_dirs) == 0:
        print("Success")
    for item in sub_dirs:
        path = os.path.abspath(master_folder + slash + item)
        if os.path.isdir(path):
            merge(path, master_folder)


def merge(path, master_folder):
    if os.path.isdir(path):
        sub_items = os.listdir(path)
        for item in sub_items:
            merge(path + slash + item, master_folder)
        try:
            os.rmdir(path)
        except:
            print("Warning: Directory is not empty, cannot be deleted")
    else:
        move_file_to_master(path, master_folder)


def move_file_to_master(path, master_folder):
    split_path = os.path.split(path)
    filename = split_path[1]
    split_filename = filename.split(".")
    basename = split_filename[0]
    file_extension = ""

    for i in split_filename[1:]:
        file_extension += "." + i

    while os.path.isfile(master_folder + slash + basename + file_extension):
        basename += "9"

    new_file = master_folder + slash + basename + file_extension
    os.rename(path, new_file)

slash = '\\' if sys.platform.startswith('win') else '/'
merge_up(sys.argv[1])
