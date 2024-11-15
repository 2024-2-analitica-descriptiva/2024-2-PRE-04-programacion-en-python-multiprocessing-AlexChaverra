"""Taller presencial"""

# pylint: disable=broad-exception-raised
import fileinput
import glob
import itertools
import os
import os.path
import string
from collections import defaultdict
from multiprocessing import Pool

from toolz.itertoolz import concat  # type: ignore


#
# Lectura de archivos
#
def load_input(input_directory):
    """Funcion load_input"""

    def make_iterator_from_single_file(input_directory):
        with open(input_directory, "rt", encoding="utf-8") as file:
            yield from file

    def make_iterator_from_multiple_files(input_directory):
        input_directory = os.path.join(input_directory, "*")
        files = glob.glob(input_directory)
        with fileinput.input(files=files) as file:
            yield from file

    if os.path.isfile(input_directory):
        return make_iterator_from_single_file(input_directory)

    return make_iterator_from_multiple_files(input_directory)


#
# Preprocesamiento
#
def preprocessing(x):
    """Preprocess the line x"""
    x = x.lower()
    x = x.translate(str.maketrans("", "", string.punctuation))
    x = x.replace("\n", "")
    return x