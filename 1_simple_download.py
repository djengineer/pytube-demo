from pytube import Playlist, YouTube
import os

# This script will take a URL playlist and download to the dl_files folder


# https://stackoverflow.com/questions/65683517/how-do-you-download-a-playlist-from-youtube-using-pytube

video_link = ""
yt = YouTube(video_link)
stream = yt.streams.get_highest_resolution()
stream.download()

# This section is for downloading a playlist
# play_list = Playlist('PAYLIST LINK')
# for video in play_list.videos:
#     video.streams.first().download()

