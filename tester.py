import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter

def apply_blur():
    # Capture the content of the frame as an image
    image = ImageGrab.grab(bbox=root.winfo_rootx(), root.winfo_rooty(), root.winfo_rootx() + frame.winfo_width(), root.winfo_rooty() + frame.winfo_height())

    # Apply a blur filter to the captured image
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=10))

    # Convert the blurred image to PhotoImage format
    blurred_photo = ImageTk.PhotoImage(blurred_image)

    # Display the blurred image in a label
    blurred_label.config(image=blurred_photo)
    blurred_label.image = blurred_photo

# Create the main window
root = tk.Tk()
root.geometry("400x300")

# Create a frame
frame = ttk.Frame(root, width=400, height=300)
frame.pack()

# Create a button to apply the blur effect
blur_button = ttk.Button(root, text="Apply Blur", command=apply_blur)
blur_button.pack()

# Create a label to display the blurred image
blurred_label = ttk.Label(root)
blurred_label.pack()

# Import the necessary modules for capturing screen content
try:
    from PIL import ImageGrab
except ImportError:
    import pyscreenshot as ImageGrab

# Run the main loop
root.mainloop()
