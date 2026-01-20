import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk
import time

root = tk.Tk()
root.title("Image Slideshow Viewer")

#list of image faths

image_paths = [
    r'/Users/lokesh/Pictures/file_00000000bdc462309d578faf8d9c9ff0.png',
    r'/Users/lokesh/Pictures/file_0000000033a861f7bacf77c1b7d65be3-min.png',
    r'/Users/lokesh/Pictures/Photo on 01-11-24 at 10.48 AM.jpg',
    r'/Users/lokesh/Pictures/IMG_20250327_190110 copy.jpg'
]

#Resize images and store them in a list 

image_size = (1080, 720)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

label = tk.Label(root)
label.pack()
()

def update_image():
    for photo in cycle(photo_images):
        label.config(image=photo)
        root.update()
        time.sleep(2)  # Display each image for 2 seconds

def start_slideshow():
    for _ in range(len(photo_images)):
        update_image()

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()

