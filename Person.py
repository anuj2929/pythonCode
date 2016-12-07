'''
Created on Dec 5, 2016

@author: anuj.b.rastogi
'''
'''
from _ast import If

class Person(object):
    variable = "this is my varibale"
    
    def __init__(self,firstName="",lastName=""):
        self.firstName=firstName
        self.lastName=lastName
        
    def __str__(self):
        return self.firstName + " " + self.lastName
    

if __name__ == "__main__" : 
    p=Person("anuj","rasotig")
    print p
    '''
"""    

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
for item in movies:
    if isinstance(item, list):
        for item_1 in item:
            if isinstance(item_1, list):
                for item_2 in item_1:
                    print item_2
    else:
        print item
"""
"""
import sys
print sys.path"""
"""
try:
    data=open("text.txt")
    for lines in data:
        print lines
    data.close()
except:
    print "error"
    """
"""
man=[]
other=[]
try:
    data=open("text.txt")
    for lines in data:
        (part1,part2) = lines.split(":")
        part1=part1.strip()
        part2=part2.strip()
        print part1+" said: "+ part2
        if part1 == "Man":
            man.append(part2)
        else:
            other.append(part2)
    data.close()
except:
    print "Erro occured"
print man
print other

data=open("out.txt","a")
print >>data, other
data.close()
"""
"""
import pickle
with open("b.pickle","wb") as writeFile:
    pickle.dump(["this is the line","ok this is another"], writeFile)
with open("b.pickle","rb") as readFile:
    a_list=pickle.load(readFile)
print a_list
"""
""" files
def sanitize(tempStr):
    if "-" in tempStr:
        splitter="-"
    elif ":" in tempStr:
        splitter=":"
    else:
        return tempStr
    (mins,secs)=tempStr.split(splitter)
    return mins+"."+secs
    
jamesData=[]
julieData=[]
mikeyData=[]
sarahData=[]
unique_jamesData=[]
try:
    with open("james.txt","r") as jamesFile,open("julie.txt","r") as julieFile,open("mikey.txt","r") as mikeyFile,open("sarah.txt","r") as sarahFile:
        jamesDataTemp=jamesFile.readline().strip().split(",")
        julieDataTemp=julieFile.readline().strip().split(",")
        mikeyDataTemp=mikeyFile.readline().strip().split(",")
        sarahDataTemp=sarahFile.readline().strip().split(",")
        for item in jamesDataTemp:
            sanitizedTime=sanitize(item)
            if not unique_jamesData.__contains__(sanitizedTime):
                unique_jamesData.append(sanitizedTime)
        #jamesData=sorted([sanitize(items) for items in jamesDataTemp])
        print sorted(unique_jamesData)[0:3]
except:
    print "error"
"""
distances={"sawe",1.1,"sadwe",1.1}
print distances         