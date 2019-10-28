from pydub import AudioSegment
from pydub.playback import play
import sounddevice as sd
import soundfile as sf
import pandas as pd
#import imageio
#imageio.plugins.ffmpeg.download() 
import moviepy
from moviepy import editor
from moviepy.editor import *

############################################################################
#Slice wav audios into smaller pieces
#Specify name of Audio that is being sliced
name = "irma2"
#Specify location of audio that will be sliced
audioPath = "/home/luis/Documents/GT_luis_audio/"+name+".MP4"
#Specify pathname of folder where sliced audios will be saved
destPath = "/home/luis/Documents/GT_luis_audio/"

#This counter is the one that specifies in which number of sliced audio you
#left off. Make sure to change it accordingly.
counter = 5

#declare lists that will hold filenames, filesizes and transcripts
filenames = []
filesizes = []
transcripts = []
#declare dictionary that will include the lists above
myDict = {}

check = input("Have you changed the value of counter[y/n]?")
if(check.lower() == 'y'):
    #Iterate infinetely until user inputs 0 and 0.
    print("To quit enter 0 for start and end")
    print("Please enter your times in seconds")
    while counter > 0:
        start = input("Start of slice: ")
        end = input("End of slice: ")
        if(start == '0' and end == '0'):
            break;
        
        #tempAudio = data[int(start)*48000:int(end)*48000]
        #sd.play(tempAudio, fs)
        print(start,end)
        
        clip = VideoFileClip(audioPath).subclip(float(start), float(end))
        audio = clip.audio
        audio.preview()
        
        save = input("Save[y/n]? ")
        if save.lower() == 'y':
            #Get transcript and append
            transcript = input("Type transcript: ")
            if transcript == None:
                print("Transcript is equal to None.")
                break
            else:
                transcripts.append(transcript)
                
            #append filename
            filename = "{:05d}_".format(counter)+name+".wav"
            filenames.append(filename)
            
            #append filesize
            filesize = audio.fps*4*(float(end)-float(start))+78.0#bytes
            filesizes.append(int(filesize))
            
            #Save sliced audio
            audio.write_audiofile(destPath+filename)
            counter+=1
        else:
            print("File not saved")
            
    #read csv where GT information is stored
    data = pd.read_csv("/home/luis/Documents/GT_luis_audio/info.csv", usecols=['wav_filename','wav_filesize', 'transcript'])
    #Store filenames, filesizes and transcript in my dictionary
    myDict['wav_filename'] = filenames
    myDict['wav_filesize'] = filesizes
    myDict['transcript'] = transcripts
    #Conver dictionary into pandas dataframe
    myDF = pd.DataFrame.from_dict(myDict)
    #Append to information extracted from csv and save new-concatenated dataframe
    data = data.append(myDF)
    data.to_csv('/home/luis/Documents/GT_luis_audio/info.csv', index=False)
    
else:
    print("Please do so.")

