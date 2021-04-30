from src.FireFoxCookieMonster import FireFoxCookieMonster

def main():
    print("hello friend")

    databaseloc = 'cookies'

    firefoxCookieMonster = FireFoxCookieMonster(databaseloc)

    firefoxCookieMonster.openDatabase()


if __name__ == "__main__":
    main()
