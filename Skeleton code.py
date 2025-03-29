from tkinter import *
from pytube import YouTube
import vlc
import pygame
import os

root=Tk() #creates main window
root.title("muSICK")
root.geometry("500x500")

pygame.mixer.init() #sets up the audio system

menubar =Menu(root) #creates menu bar attached to the root window
root.config(menu = menubar) #attach menubar as the main menu bar in window

file_menu = Menu(menubar, tearoff=0) #takmau itu line + creates submenu
file_menu.add_command(label="Volume")
file_menu.add_command(label="Settings")
file_menu.add_separator()
file_menu.add_command(label="Exit", command= root.quit)

menubar.add_cascade(label="Settings", menu= file_menu)# the file button

#listbox
songlist = Listbox(root, bg="black",)
songlist.pack()


root.mainloop()
