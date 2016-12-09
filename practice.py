'''
Created on Dec 9, 2016

@author: anuj.b.rastogi
'''
import sqlite3

conn= sqlite3.connect("tutorial.db")
c = conn.cursor()

def createTable():
    c.execute("CREATE TABLE example(Language VARCHAR,Version REAL,Skill TEXT)")

def enterData():
    c.execute("INSERT INTO example VALUES('python',2.7,'beginner')")
    c.execute("INSERT INTO example VALUES('c++',3.4,'intermediate')")

def enterDynamicData(language,version,skill):    
    c.execute("INSERT INTO example(Language,Version,Skill) VALUES(?,?,?)",(language,version,skill))
"""
lang= raw_input("What language?")
version= float(raw_input("what version"))
skill= raw_input("What is your skill level?")

enterDynamicData(lang, version, skill)
"""
def readData():
    query="SELECT * FROM example WHERE Language=?"
    for row in c.execute(query,[("python")]):
        print row
    
print "calling readData"



conn.commit()
