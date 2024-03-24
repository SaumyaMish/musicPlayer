from tkinter import *
from tkinter import filedialog, ttk
from pygame import mixer
from PIL import Image,ImageTk
import os

#screen setup
window = Tk()
window.title("Music Player")
window.geometry("920x670+290+85")
window.config(bg="#0f1a2b")
window.resizable(False,False)

# Initialize Pygame Mixer
mixer.init()

#------------------------ Functions------------------------#
def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music_title.config(text=music_name)

#------------------------ Labels and icons ------------------------#

#labels
bg_img = Image.open("images/bg.png").resize((390,300),Image.ANTIALIAS)
bg_img= ImageTk.PhotoImage(bg_img)
Label(image=bg_img,bg="#0f1a2b").place(x=25, y=25)

music_title = Label(text="Select your Favourite song....",font=("arial",15),fg="white",bg="#0f1a2b")
music_title.place(x=150,y=400,anchor=W)


#buttons

# Specify the width and height of icon
icon_size = (80,80)

play_btn = Image.open("images/play.png").resize(icon_size, Image.ANTIALIAS)
play_btn = ImageTk.PhotoImage(play_btn)
Button(image=play_btn,bg="#0f1a2b",bd=0,command=play_song).place(x=300,y=450)

pause_btn = Image.open("images/pause.png").resize(icon_size,Image.ANTIALIAS)
pause_btn = ImageTk.PhotoImage(pause_btn)
Button(image=pause_btn,bg="#0f1a2b",bd=0,command=mixer.music.pause).place(x=450,y=450)

resume_btn = Image.open(("images/resume.png")).resize((65,65),Image.ANTIALIAS)
resume_btn  = ImageTk.PhotoImage(resume_btn)
Button(image=resume_btn, bd=0,command=mixer.music.unpause).place(x=600,y=455)

#____________frame____________#

#music frame
music_frame = Frame(bd=1,relief=RIDGE)
music_frame.place(x=450,y=25,height=250,width=450)

# background of frame
# menu_img = Image.open("images/menu.png").resize((480,250),Image.ANTIALIAS)
# menu_img = ImageTk.PhotoImage(menu_img)
# Label(music_frame,image=menu_img,bg="#0f1a2b").pack()

Button(text = "Open Folder",width=15,height=2,font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=450,y=280)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame,width=100,font=("airal",10),bg="#1A6176",fg="white",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)


window.mainloop()