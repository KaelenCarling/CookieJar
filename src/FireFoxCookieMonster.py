import sqlite3


class FireFoxCookieMonster:

    def __init__(self, location):
        self.dataBaseLoc = location
        self.dataBase = sqlite3.connect('{}.sqlite'.format(self.dataBaseLoc))

    def openDatabase(self):
        self.dataBase = sqlite3.connect('{}.sqlite'.format(self.dataBaseLoc))

        curse = self.dataBase.cursor()

        query = 'SELECT * FROM moz_cookies ORDER BY id;'

        curse.execute(query)

        row = curse.fetchone()
        #row = curse.fetchall()
        print(row)

        self.dataBase.commit()
        self.dataBase.close()
