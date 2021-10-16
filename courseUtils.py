"""
A set of helper functions to rip apart and reorganize a D2L assignment file
"""
import lzma as lz
# ==============================================================================
# File             : main.py
#
# Current Author   : Robert Hewlett
#
# Previous Author  : None
#
# Contact Info     : rob.hewy@gmail.com
#
# Purpose          : Unpack and organize a D2L dropbox file
#
# Dependencies     : courseUtils, StudentInfo,
#                    7z install C:\apps\7-Zip\7z.exe'
#
# Modification Log :
#    --> Created 2019-09-19 (rh)
#    --> Updated YYYY-MM-DD (fl)
#
# =============================================================================
import os as o
import os.path as p
import shutil as su
import subprocess as sp
import zipfile as z
from typing import List

from StudentInfo import StudentInfo

StudentList = List[StudentInfo]
pathFor7z = 'C:\\apps\\zip7\\7z.exe x'

def hasStudentFilePattern(fileName: str) -> bool:
    """
    Check a file name to see if it has the D2L assignment file
    pattern --> number underscore number space hyphen space, etc 
    """
    hasPattern = False
    parts = str(fileName).replace(' ', '').split('-')
    if(len(parts) >= 3):
        if( parts[0].isnumeric() and parts[1].isnumeric()):
            hasPattern = True
    return hasPattern

def stripD2lPrefix(fileName: str) -> str:
    """
    Remove the D2L assignment pattern from the string - 
    number underscore number space hyphen space 
    """
    start = str(fileName).index(' - ')
    start += 3
    #===============================================
    # my first practical slice of my python career
    #===============================================
    return(fileName[start:])

def makeStudentList(dirPath: str) -> List[StudentInfo]:
    """
    Create a unique list of students based on the files
    extracted from a downloaded D2L bulk assignment file
    """
    studentList = []
    #====================================================
    # Cycle for all files in the working directory
    #====================================================
    for aFile in o.listdir(dirPath):
        if (hasStudentFilePattern(aFile)):
            chopped = stripD2lPrefix(aFile)
            print(chopped)
            parts = chopped.split('_')
            tempStud = StudentInfo(parts[1], parts[2], parts[0])
            if tempStud not in studentList:
                studentList.append(tempStud)
    return(studentList)

def makeStudentDirs(parentDir: str, studentList: StudentList):
    """
    Make the student directories
    """
    stud = StudentInfo()
    #====================================================
    # Make the student directories based on the list
    # using the same pattern as the dropbox 
    # currently last name sort in D2L
    #====================================================    
    for stud in studentList:
        studentDir = stud.studentDir()
        print(f'Making dir {studentDir} in {parentDir}')
        fullPath = p.join(parentDir, studentDir)
        if(not p.exists(fullPath)):
            o.mkdir(fullPath)

def moveStudentFiles(parentDir: str, studentList: StudentList):
    """
    Move the student files into the student directories
    """
    #====================================================
    # move the student files to the directories
    #====================================================
    stud = StudentInfo()
    
    for stud in studentList:
        studentDir = stud.studentDir()
        print(f'Moving files to {studentDir}')
        for aFile in o.listdir(parentDir):
            fullPath = p.join(parentDir, aFile)
            newPath = p.join(parentDir, studentDir, aFile)
            if(p.isfile(fullPath)):
                print(f'{fullPath} is a file')
                if(stud.bcitID in fullPath):
                    su.move(fullPath, newPath)

def unzipDropboxFile(parentDir: str):
    """
    Unzip the main dropbox file
    """
    #====================================================
    # preserve the old working dir
    #====================================================
    oldDir = o.curdir
    o.chdir(parentDir)
    for aFile in o.listdir(parentDir):
        if(p.isfile(aFile) and '.zip' in aFile):
            #====================================================
            # Unzip the dropbox file
            #====================================================
            with z.ZipFile(aFile, 'r') as dropboxZip:
                dropboxZip.extractall(parentDir)
    #====================================================
    # change back to the old dir
    #====================================================
    o.chdir(oldDir)

def unzipStudentFiles(parentDir: str, studentList: StudentList):
    """
    Unzip any student files
    """
    zipLogFileName = 'zip.log'
    #====================================================
    # preserve the old working dir
    #====================================================
    oldDir = o.curdir
    #====================================================
    # move the student files to the directories
    #====================================================
    stud = StudentInfo()

    for stud in studentList:
        unZippedDirCount = 1
        fullStudentDir = p.join(parentDir, stud.studentDir())
        zipLogFile = p.join(fullStudentDir, zipLogFileName)
        o.chdir(fullStudentDir)
        #====================================================
        # Get each file and see if its a type of zipped file
        # 7z, rar, zip
        #====================================================
        for aFile in o.listdir(fullStudentDir):
            unZippedDirName = f'unzipped_{unZippedDirCount:03d}'
            unZippedDir = p.join(fullStudentDir, unZippedDirName)
            print(aFile)
            if p.isfile(aFile):
                fileParts = aFile.split('.')
                fileExtension = fileParts[len(fileParts)-1]
                if fileExtension.lower() in ['7z', 'zip', 'rar'] :
                    fullStudentFile = p.join(fullStudentDir, aFile)
                    #====================================================
                    # Unzip the dropbox file
                    #====================================================
                    cmd = f'{pathFor7z} \"{fullStudentFile}\" -o\"{unZippedDir}\"'
                    print(f'Trying {cmd} ...')
                    sp.call(cmd)
                    #====================================================
                    # log which file went into which directory
                    #====================================================
                    with open(zipLogFile, 'a') as logFile:
                        logFile.write(f'{aFile} unzipped in {unZippedDirName}\n')
                    unZippedDirCount += 1
    #====================================================
    # change back to the old dir
    #====================================================
    o.chdir(oldDir)
# =============================================
# AD 99 - Run stuffer
# =============================================
if __name__ == "__main__":
    print('This module in not meant to be runnable; just IKEA for code')
    print('Instead, try running main.py in the terminal')