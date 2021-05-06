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
        root.grid_rowconfigure(0, weight=0)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=0)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=0)

        root.minsize(width=700, height=420)

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
        searchButton.grid(row=0, column=0, sticky='NEW')
        searchQuery.grid(row=0, column=1, sticky='NEW')
        cookiesDisplayBox.grid(row=1, column=0, columnspan=2, sticky='NSEW')
        #cookiesDisplayBox.pack(fill='both', side='left', )
        cookieScrollbar.grid(row=1, column=2, sticky='NSW')


        cookiesDisplayBox.insert(END, processDictionary(cookieDict))
        cookiesDisplayBox['yscrollcommand'] = cookieScrollbar.set

    # simple function to retrieve the cookies into a dictionary


if __name__ == "__main__":
    root = Tk()

    # MainApplication(root).pack(side='top', fill='both', expand=True)
    MainApplication(root)

    root.mainloop()
