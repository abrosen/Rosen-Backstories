import re
import os

def printBackstories(files):
    titles = []
    backstories = [] 
    for file in files:
        text = open("./Defs/BackstoryDefs/"+file,"r").read()
        backstories += re.findall(r"<description>(.*)</description>",text, re.MULTILINE)
        titles += re.findall(r"<title>(.*)</title>",text,re.MULTILINE) 
    for t,b in zip(titles,backstories):
        print(t.strip().capitalize(),"-",b.strip(),"\n")
    print("Total:",len(titles))
all_files = os.listdir("./Defs/BackstoryDefs/")
files = []
for f in all_files:
    if f[-3:]== "xml":
        files.append(f)
printBackstories(files)