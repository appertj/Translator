##############################################################################
# Authors: Kevin Mitchel, Josiah Appert & Liam Meredith
#
# Sub Date: 5/28/2023
#
# Project: CIS-133Y Lab 8
#
# Description: GUI program to convert Farenheit to Celcius
#              and translate English to Spanish
#
# Input: Degrees Farenheit, Words in English
#
# Output: Degrees Celcius, Words in Spanish
#
# Contributions:  Josiah - Added FarenheitToCelciusApp.py and
#                          farenheit_to_celcius_app.ui and integrated into
#                          main.py
# Kevin - Formatting, Header, Comments, and some of the about.ui file
#
# Liam  - Added EnglishToSpanishApp.py, the english_to_spanish.ui, and
#         integrated into main.py
#
# Sources: Textbook, Pycharm instructions site, Module 8 lessons
#
##############################################################################
import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from FarenheitToCelciusApp import FarenheitToCelciusApp
from EnglishToSpanishApp import EnglishToSpanishApp


# Main Window for the team calculator project.
# To add a new tab, create an App object with a get_top_frame method.
# Then, add the app to the __main_notebook, along with a name for the tab.
class MainApp:

    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Calculator created by Josiah
        farenheit_to_celcius_app = FarenheitToCelciusApp(self.__mainwindow)
        self.__main_notebook.add(farenheit_to_celcius_app.get_top_frame(),
                                 text="Farenheit to Celcius")

        # Third calculator by Liam
        english_to_spanish_app = EnglishToSpanishApp(self.__mainwindow)
        self.__main_notebook.add(english_to_spanish_app.get_top_frame(),
                                 text="English to Spanish")

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()
