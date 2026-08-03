# from tkinter import *
# root = Tk()

# photo = PhotoImage(file="photo.png")
# label = Label(root, image=photo)
# label.pack()
# root.mainloop()
import urllib.request

# The target image URL
url = "https://w7.pngwing.com/pngs/445/734/png-transparent-mythical-phoenix-watercolor-resplendent-flaming-phoenix-bird-thumbnail.png"

# Add a header so the server thinks a web browser is making the request
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

print("Downloading photo...")

# Open the URL and save the binary data to a file
with urllib.request.urlopen(req) as response:
    with open("photo.png", "wb") as out_file:
        out_file.write(response.read())

print("Download complete! Your true 'photo.png' is ready to use.")


