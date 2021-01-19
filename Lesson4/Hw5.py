import os
import sys


path = r'c:\Users\Yasha\Desktop\goit-python\Lesson1\hw3'

images = []
video = []
docs = []
music = []
unknown_files = []

def folder(path, level=1):
    
    for i in os.listdir(path):
        
        if os.path.isdir(path+'\\' + i):
            folder(path+'\\' + i, level + 1)
        
        if i.endswith("jpeg") or  i.endswith("png") or  i.endswith("jpg"):
                images.append(i)
        
        elif i.endswith("avi") or i.endswith("mp4") or  i.endswith("mov"):
            video.append(i)
        
        elif i.endswith("doc") or  i.endswith("docx") or  i.endswith("txt"):
            docs.append(i)
        
        elif i.endswith("mp3") or  i.endswith("ogg") or  i.endswith("wav") or  i.endswith("amr"):
            music.append(i)
        
        else:
            unknown_files.append(i)

all_ext = set(os.path.splitext(file_ext)[-1] for file_ext in os.listdir(path))

folder(path)
print('We have this images files in all folders:', images)
print('We have this video files in all folders:', video)
print('We have this document files in all folders:', docs)
print('We have this music files in all folders:',music)
print('This files are unknown:', unknown_files)
print("In main folder we have this ext:",all_ext)
