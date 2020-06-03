# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:34:46 2020

@author: abhil
"""

import speech_recognition as sr 
  
import os 
  
from pydub import AudioSegment 
from pydub.silence import split_on_silence




fh = open("recognized.txt", "w+") 

r = sr.Recognizer() 

harvard = sr.AudioFile('noise.wav')


with harvard as source:
    audio = r.record(source)

r.recognize_google(audio)

r.recognize_sphinx(audio)

harcard1 = sr.AudioFile('noise_ctr_mb.wav')


with harcard1 as source:
    audio = r.record(source)

r.recognize_google(audio)


harcard2 = sr.AudioFile('noise_median.wav')

4
with harcard2 as source:
    audio = r.record(source)

r.recognize_google(audio)


harcard3 = sr.AudioFile('noise_mfcc_down.wav')


with harcard3 as source:
    audio = r.record(source)

r.recognize_google(audio)





