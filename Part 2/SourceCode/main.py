# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 00:44:25 2021

@author: chakati
@developer: akashan2
"""
import cv2
import os
import tensorflow as tf
import csv
from handshape_feature_extractor import HandShapeFeatureExtractor

# =============================================================================
# Get the penultimate layer for trainig data
# =============================================================================
# your code goes here
# Extract the middle frame of each gesture video

class Gesture:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class GestureFeature:
    def __init__(self, gesture: Gesture, feature):
        self.gesture = gesture
        self.feature = feature

# Gesture Name , Output Label
gestures = [Gesture("Num0", "0"), 
            Gesture("Num1", "1"),
            Gesture("Num2", "2"), 
            Gesture("Num3", "3"),
            Gesture("Num4", "4"), 
            Gesture("Num5", "5"),
            Gesture("Num6", "6"), 
            Gesture("Num7", "7"),
            Gesture("Num8", "8"), 
            Gesture("Num9", "9"),
            Gesture("FanDown", "10"),
            Gesture("FanOn",            "11"), 
            Gesture("FanOff",           "12"),
            Gesture("FanUp", "13"),
            Gesture("LightOff",         "14"), 
            Gesture("LightOn",          "15"),
            Gesture("SetThermo",        "16")
            ]

gestures2 = [Gesture("0", "0"), 
            Gesture("1", "1"),
            Gesture("2", "2"), 
            Gesture("3", "3"),
            Gesture("4", "4"), 
            Gesture("5", "5"),
            Gesture("6", "6"), 
            Gesture("7", "7"),
            Gesture("8", "8"), 
            Gesture("9", "9"),
            Gesture("DecreaseFanSpeed", "10"),
            Gesture("FanOn",            "11"), 
            Gesture("FanOff",           "12"),
            Gesture("IncreaseFanSpeed", "13"),
            Gesture("LightOff",         "14"), 
            Gesture("LightOn",          "15"),
            Gesture("SetThermo",        "16")
            ]

def get_frame(videopath, frames_path, count):
    if not os.path.exists(frames_path):
        os.mkdir(frames_path)
    cap = cv2.VideoCapture(videopath)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    frame_no= int(video_length/2)
    cap.set(1,frame_no)
    ret,frame=cap.read()
    filename = frames_path + "/%#05d.png" % (count+1)
    cv2.imwrite(filename, frame)
    return  filename


def get_feature(folder_path, input_file, count):
    extracted_frame_filename = get_frame(folder_path + input_file, "./frames", count)
    img = cv2.imread(extracted_frame_filename, cv2.IMREAD_GRAYSCALE)
    feature = HandShapeFeatureExtractor.extract_feature(HandShapeFeatureExtractor.get_instance(), img)
    return feature


def get_gesture(gesture_file_name):
    for x in gestures:
        #temp = gesture_file_name.split('.')[0]
        #temp = temp.split('-')[-1]
        temp = gesture_file_name.split("_")[0]
        if x.name == temp:
            return x
    return None

def get_gesture2(gesture_file_name):
    for x in gestures2:
        temp = gesture_file_name.split('.')[0]
        temp = temp.split('-')[-1]
        if x.name == temp:
            return x
    print("fail")
    print(gesture_file_name)
    temp = gesture_file_name.split('.')[0]
    print(temp)
    print(temp.split('-')[-1])
    return None

# =============================================================================
# Get the penultimate layer for test data
# =============================================================================
# your code goes here 
# Extract the middle frame of each gesture video

train_features = []
train_data = "./traindata/"
count = 0
for file in os.listdir(train_data):
    gesture = get_gesture(file)
    feature = get_feature(train_data, file, count)
    gesture_feature = GestureFeature(gesture, feature)
    train_features.append(gesture_feature)
    count = count + 1

# =============================================================================
# Recognize the gesture (use cosine similarity for comparing the vectors)
# =============================================================================

results_file = open('Results.csv', 'w', newline='')
fields_names = ['Label','Output']
data_writer = csv.DictWriter(results_file, fieldnames=fields_names)
test_data = "./test/"
count = 0
for file in os.listdir(test_data):
    g2 = get_gesture2(file)
    test_feature = get_feature(test_data, file, count)
    lowest = 1
    gesture = Gesture("","")
    for train_feature in train_features:
        cosine_similarity = tf.keras.losses.cosine_similarity(test_feature, train_feature.feature, axis=-1)
        if float(cosine_similarity.numpy()) < float(lowest):
            lowest = cosine_similarity
            gesture = train_feature.gesture

    data_writer.writerow({'Label': g2.name,'Output': gesture.label})
    count = count + 1