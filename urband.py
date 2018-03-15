import sys # Just for getting command line args.
import requests # For requesting the appropriate API stuff.

# -- Global Vars --

failedReq = 'Could not get response from Urban Dictionary API.'
noDefs = 'No definitions could be found.'

reqLink = 'http://api.urbandictionary.com/v0/define?term='

def quit(msg):
    print('[!] ' + msg)
    sys.exit(1)

def getWord():
    word = ''
    
    for words in sys.argv[1:]:
        word += words + ' '

    word.strip()

    return word

def reqAPI(word):
    global resp
    resp = requests.get(reqLink + word)

def parseResp(resp):
    sizeOfDefs = len(resp.json()['list'])
   
    if (sizeOfDefs < 1):
        quit(noDefs)

    numOfDefs = min(sizeOfDefs, 3)

    keys = ['author', 'definition', 'example']

    for defs in range(0, numOfDefs):
        for key in keys:
            val = resp.json()['list'][defs][key]
            
            if (key == 'author'):
                print('Author --> ' + val)
            elif (key == 'definition'):
                print('Def --> ' + val)
            elif (key == 'example'):
                print('Example --> ' + val)
        
        print('\n')


if __name__ == "__main__":
    word = getWord()

    try:
        reqAPI(word)
    except:
        quit(failedReq) 

    parseResp(resp)
