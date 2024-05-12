import tkinter as tk
from gui import setup_gui

def main():
    """It initializes the main window and set up the GUI"""
    window = tk.Tk()
    window.title('Voting Application')
    window.geometry('220x220')
    window.resizable(False, False)

    setup_gui(window)

    window.mainloop()

if __name__ == '__main__':
    main()