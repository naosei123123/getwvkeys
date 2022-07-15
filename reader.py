import validators


def readString(message):
    string = str(input(message))
    
    return string

def readLink(message):
    url = ""

    while not validators.url(url):  
        url = readString(message)  
     
    return url