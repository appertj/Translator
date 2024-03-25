# Converts farenheit to celcius
import os
import pygubu

import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "farenheit_to_celcius_app.ui")


class FarenheitToCelciusApp:
    CONVERSION = 5 / 9

    # This class uses a simple calculator to convert farenheit to celcius.

    def __init__(self, master):

        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', master)
        builder.connect_callbacks(self)

        self.__farenheit_entry = builder.get_object('farenheit_entry', master)
        self.__celcius_entry_variable = \
            builder.get_variable('celcius_entry_variable')

    def calculate(self):
        # Convert grams to ounces. If there's an error, display an error
        # message.
        try:
            farenheit = float(self.__farenheit_entry.get())
            celcius = (farenheit - 32) * self.CONVERSION
            self.__celcius_entry_variable.set("{:.2f} celcius".format(celcius))
        except ValueError:
            mb.showerror(title="Error Calculating Celcius!",
                         message="Farenheit must be a decimal number. Please \
                                  try again.")

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a
        # tabbed notebook.
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = FarenheitToCelciusApp(root)
    app.run()
