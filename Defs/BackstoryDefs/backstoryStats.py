import xml.etree.ElementTree as ET
import os

class Backstory:
    def __init__(self, defName, slot, spawnCategories, skillGains):
        self.defName = defName
        self.slot = slot
        self.spawnCategories = spawnCategories
        self.skillGains = skillGains

    def __str__(self):
        return f"{self.defName} ({self.slot}) - Skills: {self.skillGains}"


def getFileNames(path):
    all_files = os.listdir(path)
    files = []
    for f in all_files:
        if f[-3:] == "xml":
            files.append(f)
    return files
def getBackstories(filenames, originalPath):
    backstories = []
    for filename in filenames:
        path = os.path.join(originalPath, filename)
        print(path)

        
        tree = ET.parse(path)
        root = tree.getroot()
        
        for backstoryDef in root.findall("BackstoryDef"):
            defNameNode = backstoryDef.find("defName")
            defName = defNameNode.text if defNameNode is not None else "Unknown"
            
            slotNode = backstoryDef.find("slot")
            slot = slotNode.text if slotNode is not None else "Unknown"
            
            spawnCategories = []
            spawnNode = backstoryDef.find("spawnCategories")
            if spawnNode is not None:
                for li in spawnNode.findall("li"):
                    if li.text:
                        spawnCategories.append(li.text)
                        
            skillGains = {}
            skillNode = backstoryDef.find("skillGains")
            if skillNode is not None:
                for skill in skillNode:
                    try:
                        skillGains[skill.tag] = int(skill.text)
                    except (ValueError, TypeError):
                        # Handle cases where value might not be an integer
                        pass
                        
            backstories.append(Backstory(defName, slot, spawnCategories, skillGains))
       
            
    return backstories

def skillAverageAll(backstories):
    skillGainTotals = {}
    for backstory in backstories:
        for skill, gain in backstory.skillGains.items():
            if skill in skillGainTotals:
                skillGainTotals[skill] += gain
            else:
                skillGainTotals[skill] = gain
    
    for skill, total in skillGainTotals.items():
        skillGainTotals[skill] = total / len(backstories)
    return skillGainTotals

def skillAverageBySkill(backstories):
    skillGainTotals = {}
    skillCounts = {}
    for backstory in backstories:
        for skill, gain in backstory.skillGains.items():
            if skill in skillGainTotals:
                skillGainTotals[skill] += gain
                skillCounts[skill] += 1
            else:
                skillGainTotals[skill] = gain
                skillCounts[skill] = 1
    
    for skill, count in skillCounts.items():
        skillGainTotals[skill] = skillGainTotals[skill] / skillCounts[skill]
    return skillGainTotals

def skillCount(backstories):
    skillCounts = {}
    for backstory in backstories:
        for skill, gain in backstory.skillGains.items():
            if skill in skillCounts:
                skillCounts[skill] += 1
            else:
                skillCounts[skill] = 1
    return skillCounts


path1 = 'C:/Program Files (x86)/Steam/steamapps/common/RimWorld/Data/Core/Defs/BackstoryDefs/Shuffled/'
path2 = "./Defs/BackstoryDefs/"

files1 = getFileNames(path1)
print(files1)
files2 = getFileNames(path2)
print(files2)
backstories1 = getBackstories(files1, path1)
backstories2 = getBackstories(files2, path2)
print("Core (shuffled) backstory count: ", len(backstories1))
print("Occurrences  of each skill in backstories:")
print(skillCount(backstories1))
print("Skill average by skill:")
print(skillAverageBySkill(backstories1))
print("Skill averages across all backstories (no skill is 0):")
print(skillAverageAll(backstories1))
print("----------------")

print("My backstory count: ", len(backstories2))
print("Occurrences  of each skill in backstories:")
print(skillCount(backstories2))
print("Skill average by skill:")
print(skillAverageBySkill(backstories2))
print("Skill averages across all backstories (no skill is 0):")
print(skillAverageAll(backstories2))