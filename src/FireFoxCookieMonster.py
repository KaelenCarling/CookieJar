import sqlite3
import time


class FireFoxCookieMonster:

    def __init__(self, location):
        self.dataBaseLoc = location
        self.dataBase = sqlite3.connect('{}.sqlite'.format(self.dataBaseLoc))

    def retrieveData(self):
        self.dataBase = sqlite3.connect('{}.sqlite'.format(self.dataBaseLoc))

        curse = self.dataBase.cursor()

        query = 'SELECT * FROM moz_cookies ORDER BY id;'

        curse.execute(query)

        # row = curse.fetchone()
        row = curse.fetchall()

        cookieDict = {}

        #parses into a dictionary of dictionaries that contains all the values
        for record in row:

            cookieDict[str(record[00])] = {'originAttributes': str(record[1]), 'name': record[2], 'value': record[3],
                                           'host': record[4], 'path': record[5], 'expiry': record[6],
                                           'lastAccess': record[7], 'creationTime': record[8], 'isSecure': record[9],
                                           'inBrowsers': record[10], 'sameSite': record[11], 'rawSameSite': record[12],
                                           'schemeMap': record[13]}

        #print(cookieDict)

        self.dataBase.commit()
        self.dataBase.close()

        return cookieDict
