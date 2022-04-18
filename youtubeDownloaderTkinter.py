##Modules
import tkinter
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#Functions
def selectPath():
    #Allows user to select their path of download
    path = filedialog.askdirectory()
    pathLabel.config(text = path)

def downloadFile():
    #get user path
    getLink = linkField.get()
    #get the selected path
    userPath = pathLabel.cget("text")
    yt.title = ("Downloading...")
    #download the video
    mp4Video = YouTube(getLink).streams.get_highest_resolution().download()
    vidClip = VideoFileClip(mp4Video)
    vidClip.close()
    #move files to selected directory
    shutil.move(mp4Video, userPath)
    yt.title = ("Download Complete! Download Another File...")

##Window of program
yt = Tk()
title = yt.title("Video Downloader")
canvas = Canvas(yt, width = 500, height = 500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='youtube.png')

#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

##Link field
linkField = Entry (yt, width = 40, font = ('Arial', 15))
linkLabel = Label (yt, text = "Enter Download Link: ", font = ('Ariel', 15))

#Select path for saving file
pathLabel = Label(yt, text = "Select Path For Download", font = ['Ariel', 20])
selectBtn = Button (yt, text = "Select Path", bg = 'red', padx= 22, pady= 5, font= ('Arial', 15), fg= '#fff', command = selectPath)

#Add to window
canvas.create_window(250, 280, window = pathLabel)
canvas.create_window(250, 330, window = selectBtn)

##Adding widgets to window
canvas.create_window(250, 170, window = linkLabel)
canvas.create_window(250, 245, window = linkField)

#Download buttons
download_btn = Button(yt, text = "Download File!", bg = 'green', padx= 22, pady= 5, font= ('Arial', 15), fg= '#fff', command= downloadFile)
##Add to window
canvas.create_window(250, 390, window = download_btn)





yt.mainloop()