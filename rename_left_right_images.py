#!/usr/bin/env python
#
# used to rename left/right images in separate folders.
# v1.0.0
#
# To do matching I need the left and right images to be
# in the same folder and names left001/right001. So I need
# to take the matching images and move them to a common
# directory and name them correctly.
#
'''
## License

  COPYRIGHT (C) 2016 NeuroRobotic Technologies, LLC
  ALL RIGHTS RESERVED. This code is not for public use.

'''

# David Cofer
# Initial Date: 11 July 2016
# Last Updated: 11 July 2016
# http://www.NeuroRoboticTech.com/

import os
import shutil
import cv2
import numpy as np


def findImageFiles(input_dir, ending): 
  #Get the xml files in the directory
  included_extenstions = [ending]
  img_files_list = [fn for fn in os.listdir(input_dir)
                    if any(fn.endswith(ext) for ext in included_extenstions)]
  img_files = sorted(set(img_files_list))
  #print xml_files

  return img_files


input_dir = '/media/dcofer/Backup/weed_analysis/stereo_images/RGBIR_2016_10_25/raw_calibration_images/'
output_dir = '/media/dcofer/Backup/weed_analysis/stereo_images/RGBIR_2016_10_25/calibration_images/'

img_idx = 1

rgbir_files = findImageFiles(input_dir, "_rgb.png")
#print rgbir_files

for rgbir_file in rgbir_files:
  print "Processing RGBIR: " + rgbir_file

  usb_file = rgbir_file.replace("_rgb.png", "_usb_rgb.png")
  print "Processing USB: " + usb_file

  if os.path.isfile(input_dir + usb_file):
    print "USB camera file found."
    # Now load in the usb camera file and reduce its dimensions by 2 to match rgbir
    usb_img = cv2.imread(input_dir + usb_file)
    res_usb_img = cv2.resize(usb_img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

    # Save out left USB camera image
    left_img_file = "left_" + str(img_idx).zfill(4) + ".png"
    cv2.imwrite(output_dir + left_img_file, res_usb_img)

    # Copy over right RGBIR camera image
    right_img_file = "right_" + str(img_idx).zfill(4) + ".png"
    shutil.copyfile(input_dir + rgbir_file, output_dir + right_img_file)

    # Increment the image index
    img_idx = img_idx + 1

    print "Saved iamges"
  else:
    print "USB file not found on disk. Skipping images."

