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

def processDictionary(cookiesDict):
    returnString = ''

    for id in cookiesDict:
        returnString += (f'Name:{cookiesDict[id]["name"]}\n Host:{cookiesDict[id]["host"]}{cookiesDict[id]["path"]}\n Value:{cookiesDict[id]["value"]}\n\n')

    return returnString

class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # retrieve the cookies
        cookieDict = getCookies()

        # rest of the gui here

        # ensure a consistent GUI size
        self.grid_propagate(False)
        # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # title the application
        root.title('CookieJar')

        #makes the menu bar
        menuBar = Menu(root)
        fileMenu = Menu(root)
        menuBar.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_cascade(label='Open cookie file directly')

        # adds the buttons
        searchButton = Button(root, text='Search')

        # add the search
        searchQuery = Entry(root, textvariable='searchBox', width=100)

        # add cookie dictionary output
        cookiesDisplayBox = Text(root)
        cookieScrollbar = Scrollbar(root, orient=VERTICAL, command=cookiesDisplayBox.yview)

        # construct the grid of the application
        # label.grid(row=0, column=0)
        root.config(menu=menuBar)
        searchButton.grid(row=1, column=0, padx=1, pady=1)
        searchQuery.grid(row=1, column=1, columnspan=5, padx=1, pady=1)
        cookiesDisplayBox.grid(row=2, column=0, columnspan=5, padx=2, pady=2)
        cookieScrollbar.grid(row=2, column=5, sticky='NSEW')

        cookiesDisplayBox.insert(END, processDictionary(cookieDict))
        cookiesDisplayBox['yscrollcommand'] = cookieScrollbar.set

    # simple function to retrieve the cookies into a dictionary


if __name__ == "__main__":
    root = Tk()

    # MainApplication(root).pack(side='top', fill='both', expand=True)
    MainApplication(root)

    root.mainloop()
