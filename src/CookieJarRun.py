import tkinter

from FireFoxCookieMonster import *
from tkinter import *
from tkinter.ttk import *


def getCookies():
    databaseLocations = findFirefoxCookieDatabase()

    for databaseLocation in databaseLocations:
        print("Copying from " + databaseLocation)
        firefoxCookieMonster = FireFoxCookieMonster(databaseLocation)
        firefoxCookieMonster.copyDatabase()
        return firefoxCookieMonster.retrieveCookies()


class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # retrieve the cookies
        cookieDict = getCookies()

        # rest of the gui here

        # title the application
        root.title('CookieJar')

        # set default size of window
        root.geometry('500x500')

        # adds a label at the top
        label = Label(root, text='Hello Friend')

        # adds the buttons
        openButton = Button(root, text='Open cookie file')
        searchButton = Button(root, text='Search')

        # add the search
        searchQuery = Entry(root, textvariable='searchBox')

        # add cookie dictionary output
        cookiesDisplayBox = Text(root, height = 200, width = 100)

        #construct the grid of the application
        #label.grid(row=0, column=0)
        #openButton.grid(row=0, column=0)
        searchButton.grid(row=1, column=0)
        searchQuery.grid(row=1, column=2)
        cookiesDisplayBox.grid(row=2, column=0, columnspan=5)

        # print(cookieDict)

    # simple function to retrieve the cookies into a dictionary


if __name__ == "__main__":
    root = Tk()

    #MainApplication(root).pack(side='top', fill='both', expand=True)
    MainApplication(root)

    root.mainloop()
