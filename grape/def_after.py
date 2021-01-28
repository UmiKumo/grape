import json
import os
from collections import OrderedDict

def main1(json_load,after):
    fi = open("error_image.txt",'w')
    data_name = json_load.keys()            #file_before / file_after
    data_name = "".join(data_name)          #list -> str
    data_num = len(json_load[data_name])
    for i in range(data_num):
        image_num = len(json_load[data_name][i]["image"])
        for j in range(image_num):
            image_name = json_load[data_name][i]["image"][j]
            same_file = 0
            only_file = 0
            for k in range(len(after)):
                search_image_name = "/Users/homura/Desktop/grape_dateset/20190613/" + after[k] + "/" + image_name
                if os.path.isfile(search_image_name):
                    same_file += 1
                    only_file = k
            
            if same_file != 1:
                fi.write(str([json_load[data_name][i]["grapeID"],image_name,same_file]))
                fi.write("\n")
            else:
                json_load[data_name][i]["image"][j] = "/Dropbox/grape/20190613/" + after[only_file] + "/" + image_name
    fi.close()
    return json_load


def main2(json_load):
    data_name = json_load.keys()            #file_before / file_after
    data_name = "".join(data_name)          #list -> str
    data_num = len(json_load[data_name])
    for i in range(data_num):
        data_images = json_load[data_name][i]["image"]
        data_movies = json_load[data_name][i]["movie"]
        del json_load[data_name][i]["image"]
        del json_load[data_name][i]["movie"]
        json_load[data_name][i]["images"] = data_images
        json_load[data_name][i]["movies"] = data_movies

        if json_load[data_name][i]["number_of_berries"].isdecimal():
            json_load[data_name][i]["number_of_berries"] = int(json_load[data_name][i]["number_of_berries"])
        else:
            json_load[data_name][i]["number_of_berries"] = int()

        existance_of_images = 0
        image_num = len(json_load[data_name][i]["images"])
        for j in range(image_num):
            if json_load[data_name][i]["images"][j] != "":
               existance_of_images += 1

        if existance_of_images == 0:
            json_load[data_name][i]["existance_of_images"] = bool(0)
        else:
            json_load[data_name][i]["existance_of_images"] = bool(1)
    return json_load


def main_movie_after(json_load):
    data_name = json_load.keys()            #file_before / file_after
    data_name = "".join(data_name)          #list -> str
    data_num = len(json_load[data_name])
    for i in range(data_num):
        movie_name = json_load[data_name][i]["movies"]
        same_file = 0
        only_file = 0
        grapeID = json_load[data_name][i]["grapeID"]
        variety = json_load[data_name][i]["variety"]

        if movie_name != "":
            if variety == "Kyoho":
                json_load[data_name][i]["movies"] = "/Dropbox/grape/20190613/YN10101282/" + movie_name
            elif variety == "Sunverde":
                json_load[data_name][i]["movies"] = "/Dropbox/grape/20190613/YN10101281/" + movie_name
            elif variety == "Fujiminori":
                json_load[data_name][i]["movies"] = "/Dropbox/grape/20190613/YN10101321/" + movie_name
    
            for j in range(1,78):
                targetID = "SM" + str(j)
                if grapeID == targetID:
                    json_load[data_name][i]["movies"] = "/Dropbox/grape/20190531/YN10101281/" + movie_name
            for j in range(152,174):
                targetID = "SM" + str(j)
                if grapeID == targetID:
                    json_load[data_name][i]["movies"] = "/Dropbox/grape/20190531/YN10101282/" + movie_name
            for j in range(78,152):
                targetID = "SM" + str(j)
                if grapeID == targetID:
                    json_load[data_name][i]["movies"] = "/Dropbox/grape/20190531/YN10101282/" + movie_name
    return json_load


def main_images_after(json_load):
    fi = open("error_image.txt",'a')#
    data_name = json_load.keys()            #file_before / file_after
    data_name = "".join(data_name)          #list -> str
    data_num = len(json_load[data_name])
    for i in range(data_num):
        image_num = len(json_load[data_name][i]["images"])
        grapeID = json_load[data_name][i]["grapeID"]
        for j in range(image_num):
            image_name = json_load[data_name][i]["images"][j]
            if image_name != "":
                search_image_name = ""#
                for k in range(1,114):
                    targetID = "F" + str(k)
                    if grapeID == targetID:
                        json_load[data_name][i]["images"][j] = "/Dropbox/grape/20190613/441050001168/120_06/" + image_name
                        search_image_name = "/Users/homura/Desktop/grape_dateset/20190613/441050001168/120_06/" + image_name#
                for k in range(115,122):
                    targetID = "F" + str(k)
                    if grapeID == targetID:
                        json_load[data_name][i]["images"][j] = "/Dropbox/grape/20190613/441050001168/121_06/" + image_name
                        search_image_name = "/Users/homura/Desktop/grape_dateset/20190613/441050001168/121_06/" + image_name#
                for k in range(2,149):
                    targetID = "K" + str(k)
                    if grapeID == targetID:
                        json_load[data_name][i]["images"][j] = "/Dropbox/grape/20190613/441050001168/121_06/" + image_name
                        search_image_name = "/Users/homura/Desktop/grape_dateset/20190613/441050001168/121_06/" + image_name#
                if not(os.path.isfile(search_image_name)):#
                    fi.write(str([json_load[data_name][i]["grapeID"],image_name]))
                    fi.write("\n")
        if grapeID == "F114":
            json_load[data_name][i]["images"][0] = "/Dropbox/grape/20190613/441050001168/120_06/IMG_9999.JPG"
            json_load[data_name][i]["images"][1] = "/Dropbox/grape/20190613/441050001168/121_06/IMG_0001.JPG"
            json_load[data_name][i]["images"][2] = "/Dropbox/grape/20190613/441050001168/121_06/IMG_0002.JPG"
    fi.close()
    return json_load