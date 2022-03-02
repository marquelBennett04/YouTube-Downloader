##Modules
from Tkinter import *
from Tkinter import filedialog

#Functions
def selectPath():
    #Allows user to select their path of download
    path = filedialog.askdirectory()
    pathLabel.configue(text = path)


##Window of program
yt = Tk()
yt.title = ("Video Downloader")
yt.geometry = ("500x500")
canvas = yt.geometry

##Image logo
logoImage = PhotoImage(file = 'yt.png')
canvas.create_image(250, 80, image = logoImage)
logoImage = logoImage.subsample(2, 2)

##Link field
linkField = Entry (yt, width = 50)
linkLabel = Label (yt, text = "Enter Download Link: ", font = ['Ariel', 15])

#Select path for saving file
pathLabel = Label(yt, text = "Select Path For Download", font = ['Ariel', 20])
selectBtn = Button (yt, text = "Select", command = selectPath)

#Add to window
canvas.create_window(250, 280, window = pathLabel)
canvas.create_window(250, 330, window = selectBtn)

##Adding widgets to window
canvas.create_window(250, 170, window = linkLabel)
canvas.create_window(250, 220, window = linkLabel)

#Download buttons
download_btn = Button(yt, text = "Download File!")
##Add to window
canvas.create_window(250, 390, window = download_btn)





yt.mainloop()