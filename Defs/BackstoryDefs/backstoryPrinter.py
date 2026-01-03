import re
import os

def printBackstories(files):
    titles = []
    backstories = []
    total1 = 0
    total2 = 0
    for file in files:
        text = open("./Defs/BackstoryDefs/"+file,"r",encoding="utf8").read()
        titles = re.findall(r"<title>(.*)</title>",text,re.MULTILINE) 
        backstories = re.findall(r"<description>(.*)</description>",text, re.MULTILINE)
        total1 += len(titles)
        total2 += len(backstories)
        for t,b in zip(titles,backstories):
            print(t.strip().capitalize(),"-",b.strip(),"\n")
    print("----------------Total:",total1)#,total2)
all_files = os.listdir("./Defs/BackstoryDefs/")
files = []
for f in all_files:
    if f[-3:]== "xml":
        files.append(f)
printBackstories(files)