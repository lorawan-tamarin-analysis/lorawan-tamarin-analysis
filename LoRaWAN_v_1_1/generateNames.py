import os
import fileinput

oldNames = []
alternateNames = []
for version in["v1_1"]:
    for model in ["_AllSec", "", "_NoSec"]:
        for sync in ["JS_AS_Sync", "JS_AS_Desync"]:
            for appskey in ["A1", "A2"]:
                name = "LoRaWan_"+version+"_with"+sync+model+"_"+appskey
                alternateName = "LoRaWAN_"+version+"_"+sync+model+"_"+appskey
                oldNames.append(name)
                alternateNames.append(alternateName)

newNames = []
for version in ["11"]:
    for model in ["sec", "lora", "corr"]:
        for sync in ["sync", "desync"]:
            for appskey in ["fromNS", "fromJS"]:
                name = "L_"+version+"_"+model+"_"+sync+"_"+appskey
                newNames.append(name)

for i in range(len(oldNames)):
    oldName = oldNames[i]
    newName = newNames[i]
    alternateName = alternateNames[i]
    print(oldName+" --> "+newName)
    print(alternateName+" --> "+newName)
    if os.path.exists(oldName+".spthy"):
        os.rename(oldName+".spthy", newName+".spthy")

    # There is some inconsistency with whether "with" is in the
    # name of things or not. This should hopefully fix it
    # Doing inplace rewrites like this twice is embarassing.
    with fileinput.FileInput(newName+".spthy", inplace=True) as file:
        for line in file:
            print(line.replace(oldName, newName), end='')
    with fileinput.FileInput(newName+".spthy", inplace=True) as file:
        for line in file:
            print(line.replace(alternateName, newName), end='')