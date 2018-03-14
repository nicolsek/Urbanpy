import sys # Just for getting command line args.
import requests # For requesting the appropriate API stuff.

# -- Global Vars --

failedArg = 'Failed to parse argument(s).'
failedReq = 'Could not get response from Urban Dictionary API.'

reqLink = 'http://api.urbandictionary.com/v0/define?term='

def quit(msg):
    print('[!] ' + msg)
    sys.exit(1)

def reqAPI(word):
    resp = requests.get(reqLink + word)
    
try:
    global word 
    word = sys.argv[1]
except:
    quit(failedArg)

try:
    reqAPI(word)
except:
    quit(failedReq) 
