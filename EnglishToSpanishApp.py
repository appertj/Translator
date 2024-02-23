import os
import pygubu
import tkinter as tk
from translate import Translator

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "english_to_spanish.ui")


class EnglishToSpanishApp:

    # A simple translator app that will translate English to Spanish.
    # Written by Liam Meredith

    def __init__(self, master):

        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        self.__english_entry = builder.get_object('english_entry', master)
        self.__spanish_entry_variable = \
            builder.get_variable('spanish_entry_variable')

    def calculate(self):
        # Translates text to Spanish
        english = self.__english_entry.get()
        spanish = Translator(to_lang="es").translate(english)
        self.__spanish_entry_variable.set(spanish)

    def get_top_frame(self):
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = EnglishToSpanishApp(root)
    app.run()
