#!/usr/bin/env python
# -*- coding: utf-8 -*-

import def_addpoint
import json
import os
from collections import OrderedDict


target_file = "file_after.json"
points_data_file = "point7.json"
#target_file = ["file_before.json", "file_after.json"]
#points_data_file = ["project_grape_No.1-2019-09-19_#4038.json", "project_grape_No.2-2019-09-19_#4039.json", "project_grape_No.3-2019-09-19_#4042.json",
#                    "project_grape_No.4-2019-09-19_#4043.json", "project_grape_No.5-2019-09-19_#4040.json", "project_grape_No.6-2019-09-19_#4041.json", "project_grape_No.7-2019-09-19_#4044.json"]



json_open = open(target_file,'r')
json_load = json.load(json_open, object_pairs_hook=OrderedDict)
json_open.close()

json_open = open(points_data_file,'r')
json_point = json.load(json_open, object_pairs_hook=OrderedDict)
json_open.close()


data_name = def_addpoint.search_json_data_name(json_load)
#def_addpoint.addkey_points(json_load)                              #ここ、最初の1回だけ
for i in range(len(json_point)):
    image_name = json_point[i]["task"]["metadata"][0]["information"]["filename"]
    grape_place, grape_order = def_addpoint.search_json_number(json_load, image_name)

    if grape_place == 99999:
        print("error:no such file    :" + image_name)
    else:
        json_load[data_name][grape_place]["points"][grape_order]["image"] = image_name
        json_load[data_name][grape_place]["points"][grape_order]["num_centers"] = len(json_point[i]["information"])
        for j in range(len(json_point[i]["information"])):
            coordinate = [float(json_point[i]["information"][j]["points"][0][0] * json_point[i]["information"][j]["imageWidth"]), float(json_point[i]["information"][j]["points"][0][1] * json_point[i]["information"][j]["imageHeight"])]
            json_load[data_name][grape_place]["points"][grape_order]["centers"].append(coordinate)
            json_load[data_name][grape_place]["points"][grape_order]["centers"][j].append(json_point[i]["information"][j]["label"])


json_write = open(target_file,'w')
json.dump(json_load,json_write, indent = 4, sort_keys = True)
json_write.close()