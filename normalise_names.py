#! /bin/bash/python

""" normalise_names.py
This program is designed to normalise the file names of assessment submissions to
Cloud Deakin.
It is runs in a directory containing the file names and converts all pdf and
docx files as follows:
    infile::
    000000-133333 - foon - FOOO NOOOOON - 999999991 - 29 May, 2018 4444 PM - Final Report.pdf
    outfile::
    fooo_nooooon.pdf

Author: Xero
Licence: GPL v3
"""

from __future__ import print_function
from os import rename, listdir
from os.path import isfile, join

def is_interesting(somefile,  filetypes=("pdf", "docx", "doc")):
    return any(somefile.endswith(ending) or somefile.endswith(ending.upper())
                for ending in filetypes)

def get_files_of_interest(path):
    files = filter(lambda f: isfile(join(path, f)), listdir(path))
    return filter(is_interesting, files) 


def normalise_names(files):
    i = 0
    for f in files:
        print("processing {}".format(f))
        try:
            person_name = f.split("-")
            name = person_name[3].strip().lower().replace(" ", "_")
            extension = person_name[-1].split(".")[1].lower()
            new_name = ".".join((name, extension))
            rename(f, new_name)
            i += 1
        except Exception as e:
            print("Skiping {} because of {}".format(f, e))
    print("Done. processed {} files.".format(i))


if __name__ == "__main__":
    base_dir = "./"
    normalise_names(get_files_of_interest(base_dir))
