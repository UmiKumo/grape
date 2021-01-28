#!/usr/bin/env python
# -*- coding: utf-8 -*-

import def_after
import json
import os
import pprint
from collections import OrderedDict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

target_file = "file_after.json"
after = ["441050001033","441050001168","721053001088","YN10101281","YN10101282","YN10101321"]



json_open = open(target_file,'r')
json_load = json.load(json_open, object_pairs_hook=OrderedDict)
json_write = open(target_file,'w')


json_load = def_after.main1(json_load,after)

json_load = def_after.main2(json_load)

json_load = def_after.main_movie_after(json_load)

json_load = def_after.main_images_after(json_load)



json.dump(json_load,json_write,indent = 4)
json_open.close()
json_write.close()