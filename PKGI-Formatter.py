import sys
import re
from time import time 

def converter(lineTmp):
    line = lineTmp.split()
    newLine = lineTmp.split()
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{},:'\".,<>?«»“”‘’]))"
    titleString = ""
    title = False
    for l in line:
        if l in ('NOT', 'UNLOCK/LICENSE', 'LICENSE', 'BY'):
            if l in newLine:
                newLine.remove(l)
        elif l in ('REQUIRED', 'DLC'):
            if l in newLine:
                newLine[newLine.index(l)] = ""
        if(re.findall(regex, l) or l=="MISSING"):
            if l == "MISSING":
                return -1
            title = False
        if(title):
            if l in newLine:
                newLine.remove(l)
            titleString += " "+l
        if l in ('EU', 'JP', 'US', 'ASIA'):
            title = True
    if newLine[4] in ('Data', 'PKG'):
        return -1
    tmpString = ""
    tmpString += newLine[4]+","
    tmpString += "0,"
    tmpString += titleString+","
    tmpString += "not avaiable,"
    tmpString += newLine[3]+","
    tmpString += newLine[2]+","
    if len(newLine)==8:
        tmpString += newLine[7]+","
    else:
        tmpString += newLine[5]+","
    tmpString += ","
    return (tmpString)

if sys.argv[1] == 'c': 
    print("Started!")
    millisecondsStart = int(time() * 1000) 
    new_path = sys.argv[3]
    tmpStr = ""
    counterDel = 0
    counter = 0
    with open(sys.argv[2], encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            convertedStr = converter(line)
            if(convertedStr!=-1):
                tmpStr+=convertedStr+"\n"
                counter=counter+1
            else:
                counterDel=counterDel+1
        with open(new_path, "w", encoding="utf-8") as w:
            w.write(tmpStr)
        millisecondsFinish = int(time() * 1000) 
        print("Done\n"+"Total links "+str(counter)+"\nRemoved "+ str(counterDel) + " links\nTime elapsed: "+str((millisecondsFinish-millisecondsStart)/1000)+" milliseconds")
elif sys.argv[1] == 'j':
    print("Started!")
    tmp1 = ""
    tmp2 = ""
    with open(sys.argv[2], encoding = 'utf-8') as f:
        tmp1 = f.read()
    with open(sys.argv[3], encoding = 'utf-8') as f:
        tmp2 = f.read()
    with open(sys.argv[4], "w", encoding="utf-8") as w:
        w.write(tmp1+tmp2)
    print("Merged")   
