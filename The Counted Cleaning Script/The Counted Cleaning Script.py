# Written By: Austin Daigle
# Date: 11/15/2022
# Version 1.0

# READ ME:
# This script was originally modified from the first script that I developed
# to perform my inital data cleaning operation. The functions in this script 
# have been adapted to work with the formatting of these two different data sets
# (the-counted-2015.csv and the-counted-2016.csv)
#
#
# Before running this script, please read the directions on converting 
# the .csv dataset into a properly formated .txt file (Excel will be needed to process this,
# in order to prepare into the correct usable format).
#
# =========================================================================================================
#   IMPORTS:
import tkinter as tkr
from tkinter import filedialog
import re
import copy
import datetime

#=========================================================================================================
# USEFUL DATA-CLEANING FUNCTIONS

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



#=========================================================================================================
# File Chooser GUI
root = tkr.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("txt", "*.txt")])

# list to store raw file data
rawFileData = []
# list to store parsed data
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

columnHeader = rawFileData[0].split("\t")
print(columnHeader)


for x in range(1,len(rawFileData)):
      parsedFileData.append(rawFileData[x].split("\t"))

#=================================================================================================
# WRITE YOUR DATA CLEANING FUNCTION CALLS HERE 
# if you are confused on how to do this, please refer to the original script 
# and the formatting/process that I use, 95% of the cleaning function calls 
# are cross compatable here, however, keep in mind that these are two different data set 
# so different processes will be needed in order to carry this out.


#=================================================================================================
# FILE CREATION CODE

# Note this function will not override the content in a file if that file already exists
file = open("cleaned_data_set (alt-script).csv", "a")
file.write(str(columnHeader)+"\n")
for x in range(0,len(parsedFileData)):
      file.write(str(parsedFileData[x])+"\n")
file.close