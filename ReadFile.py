def readingFile(myFile):
    '''
    Reading a given file and setting the cusrsor back to 
    begining of the file
    input : file name
    output : file contents
    '''
    cursur = open(myFile)
    
    for line in cursur:
        print(line)


myFile = "C:\Testing\Python\TextFile\MyFirstFile.txt"

readingFile(myFile)