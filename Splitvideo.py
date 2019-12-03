# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:47:03 2019

@author: cboggavarapu
"""
import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt
from moviepy.editor import *

from moviepy.editor import *

def splitvideofile(VideoFileLocation,DestinationLocation):
    start = input("Enter Start time in seconds")
    End = input("Enter End time in seconds")
    step = input("Enter step time in seconds")
#    start = int(start)
#    End = int(End)
#    step = int(step)
    start = float(start)
    End = float(End)
    step = float(step)


    for i in range(int(start),int(End),int(step)):
        
        a = str(i)
        print(i+step)
        if(i+step<End):
            if(i==0):
            
                cropclip = VideoFileClip(VideoFileLocation).subclip(i,i+step+0.05)   
                cropclip.write_videofile(DestinationLocation+'/'+''+ a+''+'.mp4')
            else:
                cropclip = VideoFileClip(VideoFileLocation).subclip(i+0.05,i+0.05+step+0.05)   
                cropclip.write_videofile(DestinationLocation+'/'+''+ a+''+'.mp4')

splitvideofile('T:/mialab/users/Chaitu/new_project/results/Test4/Test4.mp4','T:/mialab/users/Chaitu/new_project/results/ZoomNew')            

