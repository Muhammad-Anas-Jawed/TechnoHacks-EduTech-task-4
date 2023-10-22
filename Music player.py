import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.init()

def add_song():
    file_path = filedialog.askopenfilename()
    file_name = os.path.basename(file_path)
    playlist_box.insert(tk.END, file_name)
    playlist.append(file_path)

def remove_song():
    selected_song_index = playlist_box.curselection()[0]
    playlist_box.delete(selected_song_index)
    playlist.pop(selected_song_index)

def play_song():
    selected_song_index = playlist_box.curselection()[0]
    selected_song = playlist[selected_song_index]
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play(loops=0)

def stop_song():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Music Player")

playlist = []

playlist_box = tk.Listbox(root, width=50)
playlist_box.pack(pady=20)

add_button = tk.Button(root, text="Add Song", command=add_song)
add_button.pack(side=tk.LEFT, padx=20)

remove_button = tk.Button(root, text="Remove Song", command=remove_song)
remove_button.pack(side=tk.LEFT)

play_button = tk.Button(root, text="Play", command=play_song)
play_button.pack(side=tk.LEFT, padx=20)

stop_button = tk.Button(root, text="Stop", command=stop_song)
stop_button.pack(side=tk.LEFT)

root.mainloop()
