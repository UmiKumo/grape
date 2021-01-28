#!/usr/bin/env python
# -*- coding: utf-8 -*-

import def_before
import json
import os
import pprint
from collections import OrderedDict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

target_file = "file_before.json"
before = ["441050001033","441050001168","721053001088","YN10101281","YN10101282","YN10101321"]



json_open = open(target_file,'r')
json_load = json.load(json_open, object_pairs_hook=OrderedDict)
json_write = open(target_file,'w')


json_load = def_before.main1(json_load,before)

json_load = def_before.main2(json_load)

json_load = def_before.main_movie_before(json_load)



json.dump(json_load,json_write,indent = 4)
json_open.close()
json_write.close()