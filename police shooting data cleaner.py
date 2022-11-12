# Written By: Austin Daigle
# Date: 11/11/2022
# Version 1.0
# Notes: This will only work fatal-police-shootings-data.csv dataset from the Washington Post (2015-2017)
# =========================================================================================================
#   IMPORTS:
#import the basic Tkinter GUI library toolkit as "tkr"
import tkinter as tkr
#import filedialog resource from the tkinter library
from tkinter import filedialog
#Import the regex library
import re
#copy module
import copy
# import dat
import datetime

#========================================================================================================
# FUCTIONS (These are for data cleaning and analysis)

# This purges duplicate rows
def removeRedundantEntries():
      originalLineCount = len(rawFileData)
      rawFileData = set(rawFileData)


# Returns a set of a given column number
def getUniqueColumnData(columnNumber): 
      uniqueValues = []
      for x in range(0,len(parsedFileData)):
            uniqueValues.append(parsedFileData[x][columnNumber])
      return set(uniqueValues)

# Performs a complete set-order analysis of the entire file (useful for finding dirty data)
def printAllCatagories():
      print("PRINTING OUT CATEGORICAL ANALYSIS:")
      for x in range(0,len(columnHeader)):
            print("-------------------------------------------------------------------------------------------------")
            print(columnHeader[x])
            print("=========================")
            print(getUniqueColumnData(x))
            print("-------------------------------------------------------------------------------------------------")

# Find and Replace all instances of a string within a given column number
def replaceInColumn(find,replace,columnNo):
      for x in range(0,len(parsedFileData)):
            if(parsedFileData[x][columnNo] == find):
                  parsedFileData[x][columnNo] = replace
# Find and Replace all instances of the words within the replace list within a column number
def replaceInColumnWithList(find,replace,columnNo):
      for x in range(0,len(parsedFileData)):
            if(str(parsedFileData[x][columnNo]) in find):
                  parsedFileData[x][columnNo] = replace   
# Find and Replace entries in a given column number with a string 
def replaceAllInColumn(replace, columnNo):
      for x in range(0,len(parsedFileData)):
            parsedFileData[x][columnNo] = replace             

# This function reduces all of the names to just the first initial
def reduceFirstNameToLetterCode():
      for x in range(0,len(parsedFileData)):
            currentName = str(parsedFileData[x][1])
            currentName = currentName.replace(" ","")
            currentName = currentName.replace("'","")
            currentName = currentName.replace('"',"")                       
            parsedFileData[x][1] = currentName[0:1]

# convert the data from the date column into only the words for each corresponding month
def reduceDateToMonthsOnly():
      for x in range(0,len(parsedFileData)):
            convertedDate = str(parsedFileData[x][2][5:7])

            parsedFileData[x][2] = datetime.date(1900, int(convertedDate), 1).strftime('%B')
#
#========================================================================================================
# DATA CLEANING SETTINGS

fixCommasInSingleQuotes = True
fixCommasInDoubleQuotes = True
commaReplacement = ";"

#=======================================================================================================

# File Chooser GUI
root = tkr.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("cvs", "*.csv")])



rawFileData = []
parsedFileData = []

# store the column header labels as a list
columnHeader = []

# Try to Read all of the data from the file into rawFileData
try:
      with open(file_path) as fp:
            line = fp.readline()
            count = 1
            while line:
                  rawFileData.append((line.strip()))
                  line = fp.readline()
                  count += 1
      print("-------------------------------------------------------------------------------------------------")
      print("USER PROVIDED FILE PATH: "+file_path)
except:
      print("[Error] No file directory path provided. Exiting program.")
      raise SystemExit       


# Create the column header labels
columnHeader = rawFileData[0].split(",")

# Trim the header names from the raw data
rawFileData = rawFileData[1:]

# If enabled: Repleace commas inside of double quotation marks
if(fixCommasInDoubleQuotes):
      for x in range(0,len(rawFileData)):
            lineToProcess = rawFileData[x]
            for quotedStatement in re.findall(r'\"(.+?)\"',lineToProcess):
                  lineToProcess = lineToProcess.replace(quotedStatement, quotedStatement.replace(",",commaReplacement))
            rawFileData[x] = lineToProcess
 
# If enabled: Repleace commas inside of single quotation marks
if(fixCommasInSingleQuotes):
      for x in range(0,len(rawFileData)):
            lineToProcess = rawFileData[x]
            for quotedStatement in re.findall(r"'(.*?)'",lineToProcess):
                  lineToProcess = lineToProcess.replace(quotedStatement, quotedStatement.replace(",",commaReplacement))
            rawFileData[x] = lineToProcess

# convert the set to a list
rawFileData = list(rawFileData)

# Parse Data into a Matrix
for x in rawFileData:
      parsedFileData.append(x.split(","))

#=======================================================================================================

# WRITE DATA CLEANING RULES HERE


# fix the armed column
replaceInColumn("","unknown weapon",4)
replaceInColumn("undetermined","unknown weapon",4)
# fix the age column
replaceInColumn("","unknown",5)
# fix the gender column
replaceInColumn("","unknown",6)
replaceInColumn("F","Female",6)
replaceInColumn("M","Male",6)
# fix the race/ethnicity column
replaceInColumn("","unknown",7)
replaceInColumn("H","Hispanic",7)
replaceInColumn("W","White",7)
replaceInColumn("O","Other",7)
replaceInColumn("B","Black",7)
replaceInColumn("A","Asian",7)
replaceInColumn("N","Native",7)
# fix the flee column
replaceInColumn("","unknown",12)

#clean and fix weapons into categories
#blunt weapons
replaceInColumnWithList(
[
'carjack',
'tire iron',
'metal pole',
'chain',
'shovel',
'flagpole',
'metal hand tool',
'piece of wood',
'metal pipe',
'metal rake',
"contractor's level",
'baton',
'metal object',
'rock',
'oar',
'flashlight',
'blunt object',
'air conditioner',
'chair',
'stapler',
'crowbar',
'brick',
'hammer',
'pick-axe',
'baseball bat',
'metal stick',
'pipe',
'pole'
],"Blunt Weapon",4)


#other
replaceInColumnWithList(
[
'hand torch',
'sharp object',
'cordless drill',
'pen',
'screwdriver',
'garden tool',
'glass shard',
'beer bottle',
'pitchfork',
'crossbow',
'spear',
'scissors',
'bean-bag gun',
'Taser',
'nail gun'
],"Other",4)

#toy weapons
replaceInColumnWithList(
[
'toy weapon',
'pellet gun'
],"Toy Weapon",4)



#bladded weapons
replaceInColumnWithList(
[
'straight edge razor',
'box cutter',
'ax',
'lawn mower blade',
'sword',
'knife',
'meat cleaver',
'chain saw',
'hatchet',
'machete',
'bayonet'
],"Bladded Weapon",4)


#explosives
replaceInColumnWithList(
[
'fireworks'
],"Explosives",4)



#Two or more weapons 
replaceInColumnWithList(
[
'baseball bat and bottle',
'baseball bat and fireplace poker',
'pole and knife',
'hatchet and gun',
'guns and explosives',
'machete and gun',
'gun and knife'
],"Two or more weapons",4)

# Misc corrections 
replaceInColumn("gun","Firearm",4)
replaceInColumn("unarmed","Unarmed",4)
replaceInColumn("motorcycle","Vehicle",4)
replaceInColumn("vehicle","Vehicle",4)
replaceInColumn("unknown weapon","Unknown Weapon",4)


# Extra Data Processing
reduceFirstNameToLetterCode()
reduceDateToMonthsOnly()

# Print unique set of all categories
printAllCatagories()
#=======================================================================================================

# Reassemble data into a new list
newFileData = []
newFileData.append(','.join(columnHeader))

print(columnHeader)
# reassmeble the parsed data into single lines
for x in range(0,len(parsedFileData)):
      newFileData.append(','.join(parsedFileData[x]))

# Take all assembled, cleaned data and create a new file
file = open("cleaned base data (fatal-police-shootings-data).csv", "a")
for x in newFileData:
      file.write(x+"\n")
file.close






