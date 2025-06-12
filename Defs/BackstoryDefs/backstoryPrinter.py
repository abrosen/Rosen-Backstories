import re
import os

def printBackstories(files):
    titles = []
    backstories = [] 
    for file in files:
        text = open(file,"r").read()
        backstories += re.findall(r"<description>(.*)</description>",text, re.MULTILINE)
        titles += re.findall(r"<title>(.*)</title>",text,re.MULTILINE)   
    for t,b in zip(titles,backstories):
        b = b.replace("[PAWN_nameDef]", "Jean Eric")
        b = b.replace("[PAWN_possessive]", "his")
        b = b.replace("[PAWN_pronoun]", "he")
        b = b.replace("[PAWN_objective]", "him")
        
        print(t.strip().capitalize(),"-",b.strip(),"\n")


all_files = os.listdir()
files = []
for f in all_files:
    if f[-3:]== "xml":
        files.append(f)
printBackstories(files)