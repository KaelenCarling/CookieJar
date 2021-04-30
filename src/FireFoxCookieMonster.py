import shutil
import sqlite3
import getpass
import os
from glob import glob


class FireFoxCookieMonster:

    def __init__(self, location):
        self.dataBaseLoc = location
        self.dataBase = sqlite3.connect('{}.sqlite'.format(self.dataBaseLoc))
        self.localDBFile = ''

        self.dataBase.close()

    def retrieveCookies(self):
        self.dataBase = sqlite3.connect('{}.sqlite'.format(self.dataBaseLoc))

        curse = self.dataBase.cursor()

        query = 'SELECT * FROM moz_cookies ORDER BY id;'

        curse.execute(query)

        # row = curse.fetchone()
        row = curse.fetchall()

        cookieDict = {}

        # parses into a dictionary of dictionaries that contains all the values
        for record in row:
            cookieDict[str(record[00])] = {'originAttributes': str(record[1]), 'name': record[2], 'value': record[3],
                                           'host': record[4], 'path': record[5], 'expiry': record[6],
                                           'lastAccess': record[7], 'creationTime': record[8], 'isSecure': record[9],
                                           'inBrowsers': record[10], 'sameSite': record[11], 'rawSameSite': record[12],
                                           'schemeMap': record[13]}

        # print(cookieDict)

        self.dataBase.commit()
        self.dataBase.close()

        return cookieDict

    def copyDatabase(self):
        searchDirectoryString = f'/home/{getpass.getuser()}/.mozilla/firefox/'

        self.localDBFile = 'FirefoxCookies.sqlite'

        cookieFileLoc = self.findCookieFile(searchDirectoryString)

        print(cookieFileLoc)

        shutil.copyfile(cookieFileLoc, self.localDBFile)



    def findCookieFile(self, directory):

        # recursively walks through the directory given
        for fileDirectory in os.walk(directory):

            # uses glob to find files which match the criteria. if you delete the *.* it will find files without
            # types (mainly directories)
            for file in glob(os.path.join(fileDirectory[0], '*.*')):

                #checks to see if it is the correct cookies file
                if 'cookies.sqlite' in file and 'cookies.sqlite-wal' not in file:
                    return file

