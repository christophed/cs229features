#!/usr/bin/python

import jsbeautifier as jsb
from bs4 import BeautifulSoup as bsoup
import sys
import pymath

def prettyPrint(soup):
    for i,script in enumerate(soup.find_all('script')):
        print jsb.beautify(str(script))

# Some concerns: 0-length lines?
def lineInfo(soup):
    # Get line lengths
    linelens = list()

    for i,script in enumerate(soup.find_all('script')):
        #print script
        currentLineLens = list()
        for line in (jsb.beautify(str(script))).split('\n'):
            currentLineLens.append(len(line)) 
        linelens.extend(currentLineLens )
        print "Script %i num lines:%i" % (i,len(currentLineLens))
    print "Max line length: %f" %(max(linelens))
    print "Standard deviation of line length: %f" %(pymath.stdev(linelens))

def countWhitespace(soup):
    whitespace = 0 
    for script in soup.find_all('script'):
        for line in script:
            whitespace += (line.count('\n') + line.count('\t') + line.count(' ')) 


if __name__=="__main__":

    if len(sys.argv) < 2:
        print "Usage: <program> <filename>"

    filename = sys.argv[1]
    openfile = open(filename, 'rb')

    soup = bsoup(openfile.read())
    openfile.close()
    
    # TODO Recursively get external scripts?

    #lineInfo(soup)
    #prettyPrint(soup)
    countWhitespace(soup)
