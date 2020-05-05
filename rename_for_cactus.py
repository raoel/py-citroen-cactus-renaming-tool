import os
import re
import sys

from unidecode import unidecode


def rename_file(from_file):
    file, extension = os.path.splitext(from_file)

    # remove special characters
    # unidecode = standing on the shoulders of giants
    file = unidecode(file)

    # replace dots with space
    file = file.replace(".", " ")

    # remove dots and other stuff
    pattern = re.compile("[^a-zA-Z0-9\ \-]", re.IGNORECASE | re.MULTILINE)
    file = pattern.sub("_", file)

    # remove double spaces
    file = file.replace("  ", " ")

    to_file = file + extension

    return to_file.strip()


def rename_do(path, file, file_renamed):
    print("{}/{} -> {}/{}".format(path, file, path, file_renamed))
    os.rename("{}/{}".format(path, file), "{}/{}".format(path, file_renamed))


def main(path) -> int:
    counter = 0
    # rename folders
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dirname in dirnames:
            dirname_renamed = rename_file(dirname)
            if dirname_renamed != dirname:
                rename_do(dirpath, dirname, dirname_renamed)
                counter += 1

    # rename files
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            file_renamed = rename_file(file)
            if file_renamed != file:
                rename_do(dirpath, file, file_renamed)
                counter += 1
    return counter


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please add a folder as parameter")
        exit(1)
    counter = main(sys.argv[1])
    print("{} files/folders have been renamed".format(counter))
