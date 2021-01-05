**# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import time
import random
import os

def main(argv):
    usageInfo = '\nUSAGE:\n\nlogGenerator.py --logFile <targetFile>\n\t[--minSleepMs <int>] [--maxSleepMs <int>] \n\t[--sourceDataFile <fileWithTextData>] [--iterations <long>]\n\t[--minLines <int>] [--maxLines <int>] \n\t[--logPattern <pattern>] [--datePattern <pattern>]'
@@ -73,6 +74,13 @@ def main(argv):
        elif opt in ("--datePattern"):
            datePattern = arg

    
    if os.path.exists(sourceDataFile):
        pass
    else:
        print("Please check if file " + sourceDataFile + " exists")
        sys.exit()


    with open (sourceDataFile, "r") as fh:
        sourceData=fh.read()
@@ -82,18 +90,24 @@ def main(argv):
    if (maxLines > totalLines):
        maxLines = totalLines

    print("######################################")
    print("### log-generator running with.....")
    print("######################################")
    print("sourceDataFile: " + sourceDataFile)
    print("logPattern: " + logPattern)
    print("datePattern: " + datePattern)
    print("sourceData lines: " + str(totalLines))
    print("minSleep: " + str(minSleep))
    print("maxSleep: " + str(maxSleep))
    print("minLines: " + str(minLines))
    print("maxLines: " + str(maxLines))
    print("######################################")
    print("")
    print("########################################")
    print("### log-generator running variables: ###")
    print("########################################")
    print("# ")
    print("# sourceDataFile:   | " + sourceDataFile)
    print("# sourceData lines: | " + str(totalLines))
    print("# ")
    print("# minSleep:         | " + str(minSleep))
    print("# maxSleep:         | " + str(maxSleep))
    print("# minLines:         | " + str(minLines))
    print("# maxLines:         | " + str(maxLines))
    print("# ")
    print("# logFile:          | " + logFile)
    print("# logPattern:       | " + logPattern)
    print("# datePattern:      | " + datePattern)
    print("########################################")
    print("")

    
    logging.Formatter.converter = time.gmtime
@@ -129,13 +143,13 @@ def main(argv):
            continue

        logger.debug(toLog[:-1])
        print(toLog[:-1])

        if (iterations > 0):
            iterations = iterations - 1
            if (iterations == 0):
                mustIterate = False


    sys.exit(0)

if __name__ == "__main__":

