from pytube import Playlist
import os

# This script will take a URL playlist and download to the dl_files folder

# https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

# https://stackoverflow.com/questions/65683517/how-do-you-download-a-playlist-from-youtube-using-pytube

#play_list = Playlist('PAYLIST LINK')
#for video in play_list.videos:
#    video.streams.first().download()

play_list_url = ""

play_list = Playlist(play_list_url)
for video in play_list.videos:
    # download the file
    # extract only audio
    video = video.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="./dl_files")
      
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
      
    # result of success
    print(video.title + " has been successfully downloaded.")