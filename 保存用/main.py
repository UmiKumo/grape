#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import math
import cv2
import def_resize
import def_ridge1d
import def_ridge2
import def_ridge3
import def_vote
import def_peak
import gist
import def_HoG
import def_cutimg
import gist



resize_k = 8
#sobel_k = 3
ridge_k = 4
vote_k = 20
gist_size = 20
image_name = "IMG_3334.JPG"


#def_resize.resize(image_name, resize_k)
image_name = "resized.JPG"
#def_ridge1d.standard_deviation(image_name, ridge_k)
g = def_ridge2.gradient(ridge_k)
#def_ridge3.ridge(g, ridge_k)
#def_vote.center_detect(g, vote_k)
reference_num = def_peak.peak_detect(0.9)
if reference_num == 0:
    print("error:detected reference_num = 0")
    sys.exit()
print("reference circle : " + str(reference_num))


x_center = []
y_center = []
detected_num = 0
img = cv2.imread("resized.JPG")
height, width = img.shape[:2]
coordinates = cv2.imread("coordinates.JPG", cv2.IMREAD_GRAYSCALE)
ret, coordinates = cv2.threshold(coordinates, 150, 255, cv2.THRESH_BINARY)
for i in range(width):
    for j in range(height):
        if coordinates[j][i] == 255:
            x_center.append(i)
            y_center.append(j)
            detected_num += 1


color_feature_train = []      #ix3
HoG_feature_train = []        #ix1764x1
gist_feature_train = []       #ix960
for i in range(detected_num):
    def_cutimg.create_pic(x_center[i], y_center[i])
    cut_img = cv2.imread("cut_img.JPG")
    height, width, channel = cut_img.shape
    j = int((width - 1) / 2 + 1)
    color_feature_train.append(cut_img[j][j])

    HoG_feature_train.append(def_HoG.get_feature("cut_img.JPG"))

    cut_img = cv2.resize(cut_img, (gist_size, gist_size))
    descriptor = gist.extract(cut_img)
    gist_feature_train.append(descriptor)


color_feature_med = []
HoG_feature_med = []
gist_feature_med = []
for i in range(len(color_feature_train[0])):
    feature = []
    for j in range(detected_num):
        feature.append(color_feature_train[j][i])
    feature.sort()
    if i % 2 == 0:
        color_feature_med.append((feature[int(detected_num / 2)] + feature[int((detected_num / 2) + 1)]) / 2)
    else:
        color_feature_med.append(feature[int((detected_num + 1) / 2)])

for i in range(len(HoG_feature_train[0])):
    feature = []
    for j in range(detected_num):
        feature.append(HoG_feature_train[j][i][0])
    feature.sort()
    if i % 2 == 0:
        HoG_feature_med.append((feature[int(detected_num / 2)] + feature[int((detected_num / 2) + 1)]) / 2)
    else:
        HoG_feature_med.append(feature[int((detected_num + 1) / 2)])

for i in range(len(gist_feature_train[0])):
    feature = []
    for j in range(detected_num):
        feature.append(gist_feature_train[j][i])
    feature.sort()
    if i % 2 == 0:
        gist_feature_med.append((feature[int(detected_num / 2)] + feature[int((detected_num / 2) + 1)]) / 2)
    else:
        gist_feature_med.append(feature[int((detected_num + 1) / 2)])








candidate_num = def_peak.peak_detect(0.8)
print("candidate circle : " + str(candidate_num))
if candidate_num < 2:
    print("error:detected candidate_num = 1")
    sys.exit()
x_center = []
y_center = []
detected_num = 0
img = cv2.imread("resized.JPG")
height, width = img.shape[:2]
coordinates = cv2.imread("coordinates.JPG", cv2.IMREAD_GRAYSCALE)
ret, coordinates = cv2.threshold(coordinates, 150, 255, cv2.THRESH_BINARY)
for i in range(width):
    for j in range(height):
        if coordinates[j][i] == 255:
            x_center.append(i)
            y_center.append(j)
            detected_num += 1

color_feature = []      #ix3
HoG_feature = []        #ix1764x1
gist_feature = []       #ix960
for i in range(detected_num):
    def_cutimg.create_pic(x_center[i], y_center[i])
    cut_img = cv2.imread("cut_img.JPG")
    height, width, channel = cut_img.shape
    j = int((width - 1) / 2 + 1)
    color_feature.append(cut_img[j][j])
    HoG_feature.append(def_HoG.get_feature("cut_img.JPG"))
    cut_img = cv2.resize(cut_img, (gist_size, gist_size))
    descriptor = gist.extract(cut_img)
    gist_feature.append(descriptor)





t_color = 4
t_HoG = 4
t_gist = 4
t_dist = 4
t_space = 10
for i in range(detected_num):
    #print(i)
    P_color = 0
    P_HoG = 0
    P_gist = 0
    P_dist = 0
    P_space = 0
    
    lc = np.corrcoef(color_feature_med, color_feature[i])[0,1]
    P_color = 1 - (1 / (1 + math.exp(8 * lc - t_color)))

    lc = np.corrcoef(HoG_feature_med, HoG_feature[i].ravel())[0,1]
    P_HoG = 1 - (1 / (1 + math.exp(8 * lc - t_HoG)))

    lc = np.corrcoef(gist_feature_med, gist_feature[i])[0,1]
    P_gist = 1 - (1 / (1 + math.exp(8 * lc - t_gist)))

    neighbor_num = 0
    l_dist = 0
    neighbor_dist = 99999
    neighbor_point = 0
    q = 0
    l_space = 0
    for j in range(detected_num):
        distance = math.sqrt((x_center[i] - x_center[j])**2 + (y_center[i] - y_center[j])**2)
        if i != j and distance < 60:
            neighbor_num += 1
            l_dist += distance

        if i != j and neighbor_dist > distance:
            neighbor_dist = distance
            neighbor_point = j

        q += distance

    if neighbor_num != 0:
        l_dist = l_dist / neighbor_num
    P_dist = 1 - (1 / (1 + math.exp(0.5 * l_dist - t_dist)))
    if P_dist > 0.5:
        P_dist = 0.5
    
    neighbor_num = 0
    l_dist_d = 0
    for j in range(detected_num):
        distance = math.sqrt((x_center[neighbor_point] - x_center[j])**2 + (y_center[neighbor_point] - y_center[j])**2)
        if i != j and distance < 60:
            neighbor_num += 1
            l_dist_d += distance
    if neighbor_num != 0:
        l_dist_d = l_dist_d / neighbor_num



    q = q / detected_num
    l_space += np.linalg.norm(color_feature[i] - color_feature[neighbor_point], ord = 2)
    l_space += np.linalg.norm(HoG_feature[i].ravel() - HoG_feature[neighbor_point].ravel(), ord = 2)
    l_space += np.linalg.norm(gist_feature[i] - gist_feature[neighbor_point], ord = 2)
    l_space += ((l_dist - l_dist_d) * q / 10)**2
    l_space = math.sqrt(l_space)
    P_space = 1 / (1 + math.exp(l_space - t_space))

    Ey = (P_color + P_HoG + 2 * P_gist + 4 * P_dist + 4 * P_space) / 12

    '''
    print(P_color)
    print(P_HoG)
    print(P_gist)
    print(P_dist)
    print(P_space)
    print(Ey)
    print()
    '''

    if Ey > 0.5:
        cv2.drawMarker(img, (x_center[i], y_center[i]), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=5)
cv2.imwrite("plot_filtered.JPG", img)