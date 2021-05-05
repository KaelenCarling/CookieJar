from FireFoxCookieMonster import *


def main():



    databaseLocations = findFirefoxCookieDatabase()

    for databaseLocation in databaseLocations:
        print("Copying from "+databaseLocation)
        firefoxCookieMonster = FireFoxCookieMonster(databaseLocation)
        firefoxCookieMonster.copyDatabase()
        print(firefoxCookieMonster.retrieveCookies())

if __name__ == "__main__":
    main()
