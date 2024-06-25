import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from classifier import classify_single, load_and_classify_file

class ClassifierApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Breast Tumor Classification")
        self.window.geometry('450x350')
        self.window.configure(background="#f7f7f7")

        self.create_ui()

    def create_ui(self):
        # Styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background="#f7f7f7", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10, "bold"), background="#4CAF50", foreground="white")
        style.configure("TEntry", font=("Arial", 10), background="#ffffff")

        # Main frame
        main_frame = ttk.Frame(self.window, padding="10", relief=tk.GROOVE)
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Adding input fields with increased spacing
        ttk.Label(main_frame, text="Mean Radius:", background="#f7f7f7").grid(row=0, column=0, sticky=tk.W, padx=(5, 20), pady=5)
        self.radius_entry = ttk.Entry(main_frame, width=25)
        self.radius_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

        ttk.Label(main_frame, text="Mean Texture:", background="#f7f7f7").grid(row=1, column=0, sticky=tk.W, padx=(5, 20), pady=5)
        self.texture_entry = ttk.Entry(main_frame, width=25)
        self.texture_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

        ttk.Label(main_frame, text="Mean Perimeter:", background="#f7f7f7").grid(row=2, column=0, sticky=tk.W, padx=(5, 20), pady=5)
        self.perimeter_entry = ttk.Entry(main_frame, width=25)
        self.perimeter_entry.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        ttk.Label(main_frame, text="Mean Area:", background="#f7f7f7").grid(row=3, column=0, sticky=tk.W, padx=(5, 20), pady=5)
        self.area_entry = ttk.Entry(main_frame, width=25)
        self.area_entry.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        ttk.Label(main_frame, text="Mean Smoothness:", background="#f7f7f7").grid(row=4, column=0, sticky=tk.W, padx=(5, 20), pady=5)
        self.smoothness_entry = ttk.Entry(main_frame, width=25)
        self.smoothness_entry.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)

        # Button to load and classify data from a file
        load_file_button = ttk.Button(main_frame, text="Load and Classify File", command=self.load_and_classify)
        load_file_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Entry to specify the number of lines to read or 'all'
        ttk.Label(main_frame, text="Lines to Read (empty for full file):", background="#f7f7f7").grid(row=8, column=0, sticky=tk.W, padx=(5, 10), pady=5)
        self.num_lines_entry = ttk.Entry(main_frame, width=15)
        self.num_lines_entry.grid(row=8, column=1, sticky=tk.W, padx=(0, 10), pady=5)

        # Button to trigger classification for single data entry
        classify_button = ttk.Button(main_frame, text="Classify", command=self.classify)
        classify_button.grid(row=6, column=0, columnspan=2, pady=10)

    def classify(self):
        classify_single(self.radius_entry, self.texture_entry, self.perimeter_entry, self.area_entry, self.smoothness_entry)

    def load_and_classify(self):
        load_and_classify_file(self.num_lines_entry)


if __name__ == "__main__":
    window = tk.Tk()
    app = ClassifierApp(window)
    window.mainloop()
