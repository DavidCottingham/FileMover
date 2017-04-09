import os
import sys
import shutil

def findFiles(fileExtensions, exclude=True, dstDir=None):
    scriptName = os.path.basename(__file__)
    copyCount = 0
    skipCount = 0
    filePathsToCopy = []

    for root, dirs, files in os.walk(os.getcwd()):
        if dstDir in dirs:
            dirs.remove(dstDir)
            # Debug
            print("Skipping destination directory", dstDir)
        if scriptName in files:
            files.remove(scriptName)
            # Debug
            print("Skipping myself:", scriptName)
        for file in files:
            if exclude:
                if not file.lower().endswith(fileExtensions):
                    filePathsToCopy.append(os.path.join(root, file))
                    copyCount += 1
                else:
                    skipCount += 1
            else:
                if file.lower().endswith(fileExtensions):
                    filePathsToCopy.append(os.path.join(root, file))
                    copyCount += 1
                else:
                    skipCount += 1
    print(skipCount, "files will be skipped.", copyCount, "files can be copied.")
    return filePathsToCopy

def copyFiles(filesList, dstDir, overwrite=False):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    print("Starting copying")
    for file in filesList:
        copyFile(file, dstDir, overwrite)

def copyFile(filepath, dstDir, overwrite=False):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    path, filename = os.path.split(filepath)
    if not overwrite:
        filename = getUniqueFilename(filename, dstDir)
    shutil.copy2(os.path.join(path, filename), os.path.join(dstDir, filename))

def getUniqueFilename(filename, dst):
    appendString = "_"
    if os.path.isfile(os.path.join(dst, filename)):
        head, ext = os.path.splitext(filename)
        # Debug
        print("Duplicate file name found")
        filename = getUniqueFilename(head + appendString + ext, dst)
    return filename

if __name__ == '__main__':
    fileExtensions = (".txt", ".png", ".jpg", ".jpeg", ".xls", ".bmp", ".doc", \
        ".docx", ".db")
    destinationDir = "vids"
    filesToCopy = findFiles(fileExtensions, dstDir = destinationDir)
    copyFiles(filesToCopy, destinationDir)
