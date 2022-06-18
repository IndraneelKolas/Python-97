
from asyncore import read
from posixpath import split


def countWordsfromFile():
    filename = "C:/Indraneel/New folder/Whitehat/sample.txt"

    numberofwords = 0
    
    file = open(filename, 'r')

    for i in file:
        words = i.split(',')
        print(words)
        numberofwords = numberofwords + len(words)
    
    print(numberofwords)

countWordsfromFile()

