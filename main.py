import tkinter as tk
from classifier_gui import ClassifierApp

if __name__ == "__main__":
    window = tk.Tk()
    app = ClassifierApp(window)
    window.mainloop()
