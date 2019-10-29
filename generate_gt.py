from pydub import AudioSegment
from pydub.playback import play
import pandas as pd

############################################################################
#Slice wav audios into smaller pieces
#Specify name of Audio that is being sliced
name = "IS-C1L1P_May11_kid1_01-01.MP4"

#Specify location of audio that will be sliced
audioPath = "E:\\"+name
#Specify pathname of folder where sliced audios will be saved
destPath = "C:\\Users\\luis\\Desktop"

#Grab audio
audio = AudioSegment.from_file(audioPath, format="mp4")

#This counter is the one that specifies in which number of sliced audio you
#left off. Make sure to change it accordingly.
counter = 56

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
        
        tempAudio = audio[float(start)*1000:float(end)*1000]
        play(tempAudio)
        
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
            filename = "{:05d}_".format(counter)+name
            filenames.append(filename)
            #append filesize
            filesize = tempAudio.frame_count()*4 #bytes
            filesizes.append(int(filesize))
            
            #Save sliced audio
            tempAudio.export(destPath+filename, format="wav")
            print("Audio saved.")
            counter+=1
        else:
            print("File not saved")
    
    #read csv where GT information is stored
    data = pd.read_csv("C:\\Users\\luis\\Desktop\\info.csv", usecols=['wav_filename','wav_filesize', 'transcript'])
    #Store filenames, filesizes and transcript in my dictionary
    myDict['wav_filename'] = filenames
    myDict['wav_filesize'] = filesizes
    myDict['transcript'] = transcripts
    #Conver dictionary into pandas dataframe
    myDF = pd.DataFrame.from_dict(myDict)
    #Append to information extracted from csv and save new-concatenated dataframe
    data = data.append(myDF)
    data.to_csv('C:\\Users\\luis\\Desktop\\info.csv', index=False)
else:
    print("Please do so.")

