#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compare two similar json files.
If some fields are missing or the value of a field is different, an error message will be displayed.

Version: 1.3.0
Github: https://github.com/leeyoshinari/Small_Tool/tree/master/pyjson
Copyright 2018-2020 by leeyoshinari. All Rights Reserved.
"""

from pyjson.pyjson import Compare

__all__ = ["compare", "compare_dict", "compare_list", "is_equal", "flag"]

C = Compare()


def compare(file1, file2, encoding='utf-8'):
    """
    To determine whether two files are the same.

    param:
        file1: compared file, the format is '.txt';
        file2: comparing file, the format is '.txt';
        encoding: coding format, default: utf-8.
    """
    C.compare(file1, file2, encoding=encoding)


def compare_dict(dict1, dict2, is_pop=True):
    """
    To deal the 'dict' type.

    param:
        dict1: compared dict, it's a dict;
        dict2: comparing dict, it's a dict;
        is_pop: whether pop the field, default True.

        When a list is in dict, if the length of list is 1, is_pop is True, otherwise, is_pop is False.
        If the length of list is larger than 1, and is_pop is True, the key and value are mismatch.
    """
    C.parser_dict(dict1, dict2, is_pop=is_pop)


def compare_list(list1, list2):
    """
    To deal the 'list' type.

    param:
        list1: compared list, it's a list;
        list2: comparing list, it's a list.
    """
    C.parser_list(list1, list2)


def is_equal(value1, value2):
    """
    To determine whether the two values are equal.
    Currently, all types of values in the json are int, float, str, dict, list, and null.
    If there are other types that affect the accuracy of the program, you need to increase
    the support for the corresponding type.

    param:
        value1: the compared value;
        value2: the comparing value.
    """
    C.is_equal(value1, value2)

def flag():
    """
    A flag that whether of two files or two values are same.
    If same, return 1, or return 0.
    """
    return C.flag
