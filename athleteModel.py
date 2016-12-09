'''
Created on Dec 8, 2016

@author: anuj.b.rastogi
'''
import pickle

from Person import Athlete

def getCoachData(fileName):
    try:
        with open(fileName,"rb") as fileData:
            line=fileData.readline().strip().split(",")
            (name,dob)=line.pop(0),line.pop(0)
            #return {"Name":name,"DOB":dob,"Times":str(sorted(set([sanitize(item) for item in line]))[0:3])}
            return Athlete(name,dob,line)
    except IOError as err:
        print "file error= "+str(err)
        return None;
    except:
        print "some error"
        return None;

def putToStore(files_list):
    all_athletes={}
    for item in files_list:
        athleteObj=getCoachData(item)
        all_athletes[athleteObj.name]=athleteObj
        try:
            with open("Athletes.pickle","wb") as itemFile:
                pickle.dump(all_athletes, itemFile)
        except:
            print "Error"
    return all_athletes

def getFromStore():
    all_athletes={}
    try:
        with open("Athletes.pickle","rb") as itemFile:
            all_athletes=pickle.load(itemFile)
    except:
        print "error"
    return all_athletes

list_files=["james.txt","julie.txt","mikey.txt","sarah.txt"]
a=putToStore(list_files)
data=getFromStore()
for each_athlete in data:
    print "Name="+data[each_athlete].name+" has dob= "+data[each_athlete].dob+" best times= "+str(data[each_athlete].top3())