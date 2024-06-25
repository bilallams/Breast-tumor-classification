import joblib
import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

# Load your pre-trained SVM model and scaler
loaded_svm_model = joblib.load("SVM_model.joblib")
loaded_scaler = joblib.load("scaler.joblib")

# Function to perform classification
def classify_single(radius_entry, texture_entry, perimeter_entry, area_entry, smoothness_entry):
    try:
        # Ensure widgets are available and not destroyed
        assert all(widget.winfo_exists() for widget in [radius_entry, texture_entry, perimeter_entry, area_entry, smoothness_entry]), "Widget does not exist!"

        input_features = [
            float(radius_entry.get()),
            float(texture_entry.get()),
            float(perimeter_entry.get()),
            float(area_entry.get()),
            float(smoothness_entry.get())
        ]
        input_features_scaled = loaded_scaler.transform([input_features])
        prediction = loaded_svm_model.predict(input_features_scaled)[0]
        result = "Malignant" if prediction == 0 else "Benign"
        messagebox.showinfo("Classification Result", f"The tumor is classified as: {result}")

        # Clear input fields after showing the result
        for entry in [radius_entry, texture_entry, perimeter_entry, area_entry, smoothness_entry]:
            entry.delete(0, tk.END)

    except AssertionError as e:
        messagebox.showerror("Widget Error", f"An error occurred due to widget access: {str(e)}")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Please enter valid numbers for all input fields. Error: {str(e)}")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")

# Function to load data from a text file and classify it
def load_and_classify_file(num_lines_entry):
    filepath = filedialog.askopenfilename(
        title="Open data file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if filepath:
        try:
            n_lines = num_lines_entry.get().strip()
            if n_lines.isdigit():  # Check if the entry is a digit and use it
                data = pd.read_csv(filepath, nrows=int(n_lines))
            elif n_lines == '':  # Check if empty
                data = pd.read_csv(filepath)
            else:
                messagebox.showerror("Input Error", "Please enter a valid number or leave empty for all lines.")
                return
            results = []
            for index, row in data.iterrows():
                features = row.values
                features_scaled = loaded_scaler.transform([features])
                prediction = loaded_svm_model.predict(features_scaled)[0]
                results.append("Malignant" if prediction == 0 else "Benign")
            result_message = "\n".join(f"Sample {i+1}: {result}" for i, result in enumerate(results))
            messagebox.showinfo("Batch Classification Results", result_message)
            num_lines_entry.delete(0, tk.END)  # Clears the entry field after displaying results
        except Exception as e:
            messagebox.showerror("Processing Error", f"An error occurred: {str(e)}")
