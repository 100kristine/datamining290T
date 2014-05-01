# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Before this, just grepped out all of the batteryInfo from my proj
import json
filename= "/Users/Artemis/Berkeley/DataminingProj/batteryInfo.txt"
newF = open("/Users/Artemis/Berkeley/DataminingProj/batteryInfo.json",'w')
with open(filename,'r') as f:
    levels = []
    temperatures = []
    voltages = []
    for line in f:
        if len(line) > 2:
            line = line.split(';')
            typ = line[3].split("|")[2]
            level = line[-1].strip("\n")
            try:
                date = line[2].split("T")[1].split(".")[0].split(":")
                date = "".join(date[:3])
                json.dump([typ,{"level":level,"date":date}],newF)
                if "level" in typ:
                    levels +=[level]
                elif "temperature" in typ:
                    temperatures +=[level]
                elif "voltage" in typ:
                    voltages +=[level]
                else:
                    pass
            except:
                #Some have invalid dates
                pass
print [list(i) for i in zip(levels,temperatures,voltages)]
newF.close()

# <codecell>


