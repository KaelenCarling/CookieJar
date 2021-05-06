import shutil
from pathlib import Path
from sqlite3 import connect
import sys
import os
from os.path import expanduser
import time


class FireFoxCookieMonster:
    def __init__(self, location):
        self.dataBaseLoc = location
        self.localDataBaseConnection = None
        self.copiedDatabaseName = 'FirefoxCookies.sqlite'



    def retrieveCookies(self):
        self.localDataBaseConnection = connect(self.copiedDatabaseName)
        curse = self.localDataBaseConnection.cursor()

        query = 'SELECT * FROM moz_cookies ORDER BY id;'
        curse.execute(query)
        # row = curse.fetchone()
        row = curse.fetchall()

        cookieDict = {}

        # parses into a dictionary of dictionaries that contains all the values
        for record in row:
            cookieDict[record[00]] = {'originAttributes': str(record[1]), 'name': record[2], 'value': record[3],
                                           'host': record[4], 'path': record[5], 'expiry': record[6],
                                           'lastAccess': record[7], 'creationTime': record[8], 'isSecure': record[9],
                                           'inBrowsers': record[10], 'sameSite': record[11], 'rawSameSite': record[12],
                                           'schemeMap': record[13]}
        self.localDataBaseConnection.close()
        return cookieDict

    def copyDatabase(self):
        shutil.copyfile(self.dataBaseLoc, self.copiedDatabaseName)



def  findFirefoxCookieDatabase():
    currentOS = sys.platform
    firefoxProfileDir = None
    targetFile="cookies.sqlite"
    databaseList = []
    returnedDataBases = []

    print()

    if currentOS.startswith('freebsd') or currentOS.startswith('linux'):
        homeDir = expanduser("~")
        firefoxProfileDir = homeDir+"/.mozilla"
    elif currentOS.startswith('win32'):
        firefoxProfileDir = str(Path.home()) +"\AppData\Roaming\Mozilla\Firefox"

    for dirName, subdirList, fileList in os.walk(firefoxProfileDir):
      #  print('Found directory: %s' % dirName)
        for fname in fileList:
            if fname == targetFile:
                foundDatabase=dirName+"/"+fname
                databaseList.append(foundDatabase)

    if len(databaseList) == 0:
        raise FileNotFoundError("No Cookie Database Files Were Found in "+ firefoxProfileDir)
    elif len(databaseList) == 1:
        #return the database without sorting or prompting the user if only one choice is available.
      return databaseList
    else:
        # we start be labeling the first entry 1
        numberOfDatabases = 1
        # sort the files in descending order of time modified
        databaseList = sorted(databaseList, key=lambda t: -os.stat(t).st_mtime)
        for databaseFile in databaseList:
            modTimesinceEpoc = os.path.getmtime(databaseFile)

            # Convert seconds since epoch to readable timestamp
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            print(str(numberOfDatabases)+". "+"Found: "+databaseFile +" (Last Modified: " + modificationTime+")")
            numberOfDatabases+=1

        userChoices = input("Please enter a comma delineated(EX: 1,3,4) choice: ").split(",")
        for choice in userChoices:
            choice=int(choice)
            returnedDataBases.append(databaseList[choice-1])
        return returnedDataBases

