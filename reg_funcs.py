#!/usr/bin/python
# Author: Luis Serrano <lserranoit@gmail.com>
# Descrption: Library to simplify the main.py code
#
import re

def find_text(text_to_search, source):
    result = re.findall(text_to_search, source)
    if result:
        return result[0]
    else:
        return False


def is_fatal(find, value):

    result = re.findall(find, value)
    if result:
        return True
    return False

def equal_elements(lista):
    """
    Recibe una lista, y devuelve un diccionario con todas las repeticiones de
    cada valor
    """
    return {i:lista.count(i) for i in lista}
