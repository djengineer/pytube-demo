from pytube import Playlist
import os

# This script will take a URL playlist and download to the dl_files folder

# https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

# https://stackoverflow.com/questions/65683517/how-do-you-download-a-playlist-from-youtube-using-pytube

#play_list = Playlist('PAYLIST LINK')
#for video in play_list.videos:
#    video.streams.first().download()

play_list_url = "https://www.youtube.com/playlist?list=PLPC1Scg9LTVJKs2nz6oZJJTKiM90vPSM6"

play_list = Playlist(play_list_url)

f = open("play_list.txt", "a")


for video in play_list.videos:
    # result of success
    print(video.title)
    f.write(video.title + "\n")
f.close()