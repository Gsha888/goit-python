import os
import sys

path = r'c:\Users\Yasha\Desktop\goit-python\Lesson1\hw3'
files = os.listdir(path)

images = []
video = []
docs = []
music = []
unknown_files = []

for i in files:
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

all_ext = set(os.path.splitext(file)[-1] for file in files)

print(images)
print(video)
print(docs)
print(music)
print(unknown_files)
print(all_ext)
