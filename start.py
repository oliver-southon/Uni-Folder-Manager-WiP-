# AUTHOR: Oliver Southon
# PURPOSE: Simple app to create a uni folder

import os

def makeFolder(path, fileName, weekCount):
    os.mkdir(path + "/" + fileName)
    os.mkdir(path + "/" + fileName + "/assignments")
    for i in range(1, weekCount + 1):
        os.mkdir(path + "/" + fileName +  "/w" + str(i))

if __name__ == "__main__": 
    myDir = input('Enter a directory to make your uni folders: ')
    shouldContinue = True
    while shouldContinue:
        fileName = input("Enter the name of your course: ")
        weekCount = int(input("How many weeks are in your course?: "))
        try:
            makeFolder(myDir, fileName, weekCount)
        except:
            print("ERROR: Could not make folder")
        restart = input("Do you wish to make another uni folder? (Y/N): ")
        if restart == "Y" or restart == "y":
            pass
        elif restart == "N" or restart == "n":
            shouldContinue = False
        else:
            print("Invalid input.")
            break

