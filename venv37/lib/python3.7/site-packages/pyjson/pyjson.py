#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compare two similar json files.
If some fields are missing or the value of a field is different, an error message will be displayed.

Version: 1.3.0
Github: https://github.com/leeyoshinari/Small_Tool/tree/master/pyjson
Copyright 2018-2020 by leeyoshinari. All Rights Reserved.
"""

import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Compare:
    def __init__(self):
        self.flag = 1  # a flag, used to determine whether two files are same.
        self.field = ['']   # a list, store the fields that traverse the dict.
        self.new_file = None
        self.raw_file = None

    def compare(self, file1, file2, encoding):
        """
        To determine whether two files are the same.
        param:
            file1: a new file;
            file2: a raw file;
            encoding: coding format, default: utf-8.
        """
        self.flag = 1  # initialize
        self.new_file = file1  # new
        self.raw_file = file2  # raw
        new_json = json.load(open(self.new_file, 'r', encoding=encoding))  # read json file
        raw_json = json.load(open(self.raw_file, 'r', encoding=encoding))

        # If new_json and raw_json are the 'dict' type or 'list' type, compare them,
        # otherwise throw an error.
        if isinstance(new_json, dict) and isinstance(raw_json, dict):
            self.parser_dict(new_json, raw_json)

        elif isinstance(new_json, list) and isinstance(raw_json, list):
            self.parser_list(new_json, raw_json)

        else:
            self.flag = 0
            logging.error('The file is not JSON.')

        # If flag is true, it means two files are the same.
        if self.flag:
            logging.info('There are the same between "{}" and "{}".'.format(self.new_file, self.raw_file))

    def parser_dict(self, dict1, dict2, is_pop=True):
        """
        To deal the 'dict' type.
        """
        for key, value in dict1.items():
            if key in dict2.keys():
                self.field.append(key)
                if isinstance(value, dict):  # dict type
                    self.parser_dict(value, dict2[key])

                elif isinstance(value, list):  # list type
                    self.parser_list(value, dict2[key])

                else:
                    self.is_equal(value, dict2[key])

            else:
                self.flag = 0
                if self.new_file or self.raw_file:
                    logging.error('The key "{}" is not in raw file "{}"'.format(key, self.raw_file))
                else:
                    logging.error('The key "{}" is not in the second file.'.format(key))

        if is_pop:
            self.field.pop()

    def parser_list(self, list1, list2):
        """
        To deal the 'list' type.
        """
        if list2:
            is_pop = True
            if len(list1) > 1:
                is_pop = False

            for n in range(len(list1)):
                if isinstance(list1[n], dict):  # dict type
                    try:
                        self.parser_dict(list1[n], list2[n], is_pop=is_pop)
                    except Exception as e:
                        self.flag = 0
                        logging.error(e)
                else:
                    self.flag = 0
                    logging.error('Exist illegal field. There is no dict in list.')

        else:
            self.flag = 0
            self.is_equal(list1, list2)


    def is_equal(self, value1, value2):
        """
        To determine whether the two values are equal.
           Currently, all types of values in the json are int, float, str, dict, list, and null.
           If there are other types that affect the accuracy of the program, you need to increase
           the support for the corresponding type.
        param:
            value1: the value of the new file;
            value2: the value of the raw file;
            field: the key in new file.
        Description:
            1 and 1.0 are equal in Python. In order to compare the values of each field
            absolutely equal, it is converted to str.
        """
        if str(value1) != str(value2):
            self.flag = 0
            if self.new_file or self.raw_file:
                logging.error('"{}" is not equal to "{}" in "{}", new file name is "{}", raw file name '
                              'is "{}"'.format(value1, value2, self.log_str(), self.new_file, self.raw_file))
            else:
                logging.error('"{}" is not equal to "{}" in "{}".'.format(value1, value2, self.log_str()))

        self.field.pop()

    def log_str(self):
        """
        Splice the fields, used for finding the error field in dict.
        """
        res = ''
        if len(self.field) > 1:
            last = self.field[-1]
            for r in self.field[1:-1]:
                res += r + '->'

            return res + last
        else:
            return ''
