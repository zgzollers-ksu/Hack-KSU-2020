import hashlib
import passwords


def find_match(options: dict, hash: list):
    for item in hash:
        if item in dict.keys():
            return dict[item]
    return "\0"


# Reads in a file name and returns a list where each line in the file is a value in the list
def read_file(file_name):
    fo = open(file_name, "r")
    password_list = fo.readlines()
    for i in range(len(password_list)):
        if i != len(password_list) - 1:
            password_list[i] = password_list[i][0:-1]
    fo.close()
    return password_list

