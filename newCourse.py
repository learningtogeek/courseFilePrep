import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

# Function to create course directory
def create_course_directory():
    course_number = course_number_entry.get()
    course_title = course_title_entry.get().replace(" ", "_")
    selected_location = location_combobox.get()
    
    if not course_number or not course_title:
        messagebox.showerror("Input Error", "Both fields must be filled out")
        return
    
    if selected_location == "Other...":
        selected_location = filedialog.askdirectory(title="Select Directory")
        if not selected_location:
            return  # User cancelled the directory selection

    # Check if the selected location exists, and create it if it doesn't
    if not os.path.exists(selected_location):
        try:
            os.makedirs(selected_location)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create directory: {str(e)}")
            return

    course_dir = os.path.join(selected_location, f"{course_number}_{course_title}")
    os.makedirs(course_dir, exist_ok=True)
    
     # Create subdirectories for each week, along with nested Lectures and Assignments subdirectories
    for i in range(1, 9):
        week_dir = os.path.join(course_dir, f"Week {i}")
        os.makedirs(week_dir, exist_ok=True)
        
        for subdir in ["Lectures", "Assignments"]:
            os.makedirs(os.path.join(week_dir, subdir), exist_ok=True)
    
    # Create subdirectories for Course Matter and Research
    for subdir in ["Course Matter", "Research"]:
        os.makedirs(os.path.join(course_dir, subdir), exist_ok=True)
    
    readme_path = os.path.join(course_dir, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {course_number} - {course_title.replace('_', ' ')}\n")
        readme_file.write(f"\nCourse materials for {course_number} - {course_title.replace('_', ' ')}.\n")
    
    # Additional subdirectory for exams
    additional_subdirs = ["Exams"]
    for subdir in additional_subdirs:
        os.makedirs(os.path.join(course_dir, subdir), exist_ok=True)
    
    readme_path = os.path.join(course_dir, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {course_number} - {course_title.replace('_', ' ')}\n")
        readme_file.write(f"\nCourse materials for {course_number} - {course_title.replace('_', ' ')}.\n")
    
    messagebox.showinfo("Success", f"Directory structure for {course_number} - {course_title.replace('_', ' ')} created successfully")

# Create the main window
window = tk.Tk()
window.title("Course Directory Creator")

# Create labels and entry fields
tk.Label(window, text="Course Number:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
course_number_entry = tk.Entry(window)
course_number_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Course Title:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
course_title_entry = tk.Entry(window)
course_title_entry.grid(row=1, column=1, padx=5, pady=5)

# Create label and combobox for location selection
tk.Label(window, text="Location:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
location_options = [os.path.expanduser("~"), os.path.expanduser("~/Desktop"), "Other..."]
location_combobox = ttk.Combobox(window, values=location_options)
location_combobox.grid(row=2, column=1, padx=5, pady=5)
location_combobox.set(location_options[1])  # Set default location to Desktop

# Create button to trigger directory creation
create_button = tk.Button(window, text="Create Directory", command=create_course_directory)
create_button.grid(row=3, columnspan=2, pady=10)

# Run the main event loop
window.mainloop()