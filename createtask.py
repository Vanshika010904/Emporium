from tkinter import *
import customtkinter

# Set appearance mode and color theme
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window
root = customtkinter.CTk()
root.title('Tkinter.com - Custom Tkinter Entry Fields')
root.geometry('700x700')
root.resizable(False, False)
# Function to submit the task
def submit():
    output_label.configure(text=f'Hello {my_entry.get()}')
    my_entry.configure(state="disabled")
    
# Function to clear the entry fields
def clear():
    my_entry.configure(state="normal")
    my_entry.delete(0, END)
    my_entry1.configure(state="normal")
    my_entry1.delete(0, END)
    output_label.configure(text="")  # Clear output label

# Label for task creation
my_label = customtkinter.CTkLabel(root, text="Create Task", font=("Helvetica", 24), text_color="black")
my_label.pack(pady=(40, 10))

# Entry field for task
my_entry = customtkinter.CTkEntry(
    root,
    placeholder_text="Task name",
    height=60,
    width=500,
    font=('Helvetica', 12),
    corner_radius=10,
    text_color="black",
    placeholder_text_color="gray",
    
    fg_color=("#d9d9d9", "#d9d9d9")
)
my_entry.pack(pady=10)

# Entry field for description
my_entry1 = customtkinter.CTkEntry(
    root,
    placeholder_text="Description",
    height=100,
    width=500,
    font=('Helvetica', 12),
    corner_radius=10,
    text_color="black",
    placeholder_text_color="gray",
    fg_color=("#d9d9d9", "#d9d9d9")
)
my_entry1.pack(pady=10)

my_entry2 = customtkinter.CTkEntry(
    root,
    # placeholder_text="Task name",
    height=200,
    width=230,
    font=('Helvetica', 12),
    corner_radius=10,
    text_color="black",
    placeholder_text_color="gray",
    
    fg_color=("#d9d9d9", "#d9d9d9")
)
my_entry2.pack(pady=10)
my_entry2.place(x=100,y=290)


my_entry3 = customtkinter.CTkEntry(
    root,
    # placeholder_text="Task name",
    height=200,
    width=230,
    font=('Helvetica', 12),
    corner_radius=10,
    text_color="black",
    placeholder_text_color="gray",
    
    fg_color=("#d9d9d9", "#d9d9d9")
)
my_entry3.pack(pady=10)
my_entry3.place(x=365,y=290)

# Submit button
my_button = customtkinter.CTkButton(root, text="Back", command=submit,fg_color="#273f74",width=230)
my_button.pack(pady=10)
my_button.place(x=100,y=510)

# Clear button
clear_button = customtkinter.CTkButton(root, text="Clear", command=clear,fg_color="#273f74",width=230)
clear_button.pack(pady=10)
clear_button.place(x=365,y=510)

# Output label to display messages
output_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
output_label.pack(pady=20)

# Start the event loop
root.mainloop()
