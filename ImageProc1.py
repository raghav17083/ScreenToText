import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
import pyimgur
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import tkinter as tk
from PIL import ImageGrab
import numpy as np
# import cv2
from PIL import Image
import ScreenGrab
import os
import json
import clipboard
#yes we can do this

exec('ScreenGrab')
CLIENT_ID = "c94258cafc45d15"
PATH = "C:\\Users\\14LIN\\Desktop\\Screenshot\\capture.png"
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")

subscription_key = "415f1df9cc3b4d3da8684c0d3d579974"
assert subscription_key

vision_base_url = "https://centralindia.api.cognitive.microsoft.com/vision/v2.0/"

ocr_url = vision_base_url + "ocr"

image_url = uploaded_image.link
print (image_url)
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'unk'}
data    = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
response.raise_for_status()

analysis = response.json()
print(analysis)
analysis=analysis["regions"]
dicky={}
licky={}
for i in analysis:
	temp=i["lines"]
	for i1 in temp:
		temp2=i1["words"]
		for i2 in temp2:
			a1 = i2["boundingBox"].split(',')#[1],i2["boundingBox"][0],i2["boundingBox"][3],i2["boundingBox"][2]
			a = int(a1[1]),int(a1[0]),int(a1[3]),int(a1[2])
			b = i2["text"]
			dicky[a]=b;
			print(i2["boundingBox"])
			print(i2["text"],end=' ')
		print()
print(dicky)
prev = 0
temp={}
for key in sorted(dicky):
	print(key[0],key[1],dicky[key])

prev = 0
d = 0
s = '' 
for key in sorted(dicky):
	new  = key[0]
	if (new - prev)< 3*d:
		licky[key[1],key[2],key[3]]=dicky[key]
	else:
		for k in sorted(licky):
			print(licky[k],end=" ")
			s+=str(licky[k])+" "
		print()
		s+='\n'
		licky={}
		licky[key[1],key[2],key[3]]=dicky[key]
	d = (new - prev)
	prev = new

clipboard.function3(s)

# dict_analysis=json.loads(analysis)
# for i in dict_analysis:
# 	print(i)
# line_infos = [region["lines"] for region in analysis["regions"]]
# word_infos = []
# for line in line_infos:
#     for word_metadata in line:
#         for word_info in word_metadata["words"]:
#             word_infos.append(word_info)
# print(word_infos)