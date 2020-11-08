import hashlib
import passwords


def find_match(options: dict, hash: list):
    matches = {}
    for item in hash:
        if item in options.keys():
            matches[item] = options[item]
            print
    return matches


# Reads in a file name and returns a list where each line in the file is a value in the list
def read_file(file_name):
    fo = open(file_name, "r")
    password_list = fo.readlines()
    for i in range(len(password_list)):
        if i != len(password_list) - 1:
            password_list[i] = password_list[i][0:-1]
    fo.close()
    return password_list


def main():
    file_contents = read_file(input("Enter filename containing hashed passwords: "))
    entropy = float(input("Enter the entropy limit (bits): "))
    # max_num = int(input("Enter the max number of passwords: "))

    passwds = passwords.generate_passwords(entropy)
    matches = find_match(passwds, file_contents)

    if len(matches) > 0:
        for match in matches.keys():
            print("{:20s}... : {}".format(match, matches[match]))

    else:
        print("No matches found")

main()