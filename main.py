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
# Dependencies     : courseUtils, StudentInfo
#
# Modification Log :
#    --> Created 2019-09-19 (rh)
#    --> Updated YYYY-MM-DD (fl)
#
# =============================================================================
import courseUtils as u

#====================================================
# Get parent dir
#====================================================
parentDir = input('Enter the folder with the dropbox file:')
u.unzipDropboxFile(parentDir)
#====================================================
# Create a blank student list
#====================================================
studentList = u.makeStudentList(parentDir)
#====================================================
# make the directories # print(studentList)
#====================================================
u.makeStudentDirs(parentDir, studentList)
#====================================================
# Move the file
#====================================================
u.moveStudentFiles(parentDir, studentList)
#====================================================
# Unpack any student zipfiles
#====================================================
u.unzipStudentFiles(parentDir, studentList)