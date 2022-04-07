
import urllib

def fetchPage(url) :
    with urllib.request.urlopen(url) as response:
        data = {""}
        text = response.read()
        print(text)

def printLength(url) :
   pass


def getOutgoingURLs(url) :
    pass






