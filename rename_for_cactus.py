import os
import re
import sys

import unidecode


def rename_file(from_file):
    # if not from_file[:3] == "05.":
    #     return ""
    # remove special characters
    file, extension = os.path.splitext(from_file)
    file = unidecode(file)
    # remove dots
    file = file.replace(".", " ")

    # remove dots and other stuff
    pattern = re.compile("[^a-zA-Z0-9\ ]", re.IGNORECASE | re.MULTILINE)
    file = pattern.sub("_", file)

    # remove double spaces
    file = file.replace("  ", " ")

    to_file = file + extension
    print("{} -> {}".format(from_file, to_file))
    return to_file


def main(path):
    # cwd = os.getcwd()
    # rename folders
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dirname in dirnames:
            dirname_renamed = rename_file(dirname)
            os.rename(
                "{}/{}".format(dirpath, dirname),
                "{}/{}".format(dirpath, dirname_renamed),
            )
    # now rename files
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            file_renamed = rename_file(file)
            os.rename(
                "{}/{}".format(dirpath, file), "{}/{}".format(dirpath, file_renamed)
            )


print(__name__)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        exit(1)
    main(sys.argv[1])
