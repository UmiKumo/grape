#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pprint
import os
from collections import OrderedDict

#json_open = open("test.json",'r')
#json_load = json.load(json_open)
#json_load = json.load(json_open, object_pairs_hook=OrderedDict)    順序を保つ場合

#print json.dumps(json_load["test"][1]["grapeID"])
print("a")
for curDir, dirs, files in os.walk("20190613"):
    print('===================')
    print("現在のディレクトリ: " + curDir)
    print("内包するディレクトリ:" + str(dirs))
    print("内包するファイル: " + str(files))
print("b")
'''
print(json_load)                   default
print json.dumps(json_load)        'u'を消せる
pprint.pprint(json_load)           整頓して見やすく
print(len(json_load["test"]))      要素数も取ってこれる
print json_load.keys()             これだけは特殊でこうしないと取れない
name = "".join(name)               list -> str


search_name = "/Users/homura/Desktop/grape_dateset/20190531撮影/441050001033/IMG_3331.JPG"
if os.path.isfile(search_name):
    print("hit")


with open("test.json", 'w') as outfile:
    json.dump(json_load, outfile, indent=4)
            or
json_open.close()                   1度閉じてから
json_open = open("test.json",'w')
json.dump(json_load,json_open,indent = 4)
'''