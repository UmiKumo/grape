#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from collections import OrderedDict

def search_json_number(json_load, image_name):
    data_name = json_load.keys()
    data_name = "".join(data_name)
    data_num = len(json_load[data_name])
    for i in range(data_num):
        for j in range(len(json_load[data_name][i]["images"])):
            if image_name in json_load[data_name][i]["images"][j]:
                return i, j
    return 99999, 99999


def search_json_data_name(json_load):
    data_name = json_load.keys()
    data_name = "".join(data_name)
    return data_name


def addkey_points(json_load):
    data_name = json_load.keys()
    data_name = "".join(data_name)
    data_num = len(json_load[data_name])
    for i in range(data_num):
        json_load[data_name][i]["points"] = []
        for j in range(len(json_load[data_name][i]["images"])):
            json_load[data_name][i]["points"].append({})
            json_load[data_name][i]["points"][j]["centers"] = []
    return json_load
