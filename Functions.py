def countWordFromFile():
    fileName = input("Enter the file name")
    numberOfwords = 0
    file = open(fileName)
    for lines in file:
        words = lines.split()
        numberOfwords = numberOfwords + len(words)
    print(numberOfwords)
    
countWordFromFile()