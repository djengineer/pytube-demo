from pytube import Playlist, YouTube
import os, sys
import argparse

# https://pytube.io/en/latest/api.html
# https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

# https://stackoverflow.com/questions/65683517/how-do-you-download-a-playlist-from-youtube-using-pytube

# argsparse
# https://docs.python.org/3/howto/argparse.html
# https://stackoverflow.com/questions/15836713/allowing-specific-values-for-an-argparse-argument
# https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
# https://stackoverflow.com/questions/28638813/how-to-make-a-short-and-long-version-of-a-required-argument-using-python-argpars


def dl_playlist(play_list_url,mp3_only):
    '''
    mp3_only expects Boolean True or False
    '''
    play_list = Playlist(play_list_url)
    f = open("./dl_files/0_download_list.txt", "a")
    for video in play_list.videos:
        # download the file
        # extract only audio
        if mp3_only == False:
            video = video.streams.get_highest_resolution()
            out_file = video.download(output_path="./dl_files",skip_existing= True)
            print(video.title + " downloaded.")
            f.write(video.title.strip() + "\n")
        elif mp3_only == True:
            video = video.streams.filter(only_audio=mp3_only).first()
             # save the file
            out_file = video.download(output_path="./dl_files",skip_existing= True)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            # result of success
            print(video.title + " downloaded.")
            f.write(video.title.strip() + ".mp3\n")      
    f.close()


def dl_single(video_link,mp3_only):
    f = open("./dl_files/0_download_list.txt", "a")
    yt = YouTube(video_link)
    if mp3_only == False:
        video = yt.streams.get_highest_resolution()
        out_file = video.download(output_path="./dl_files",skip_existing= True)
        print(video.title + " downloaded.")
        f.write(video.title.strip() + "\n")
    elif mp3_only == True:
        video = yt.streams.filter(only_audio=mp3_only).first()
        # save the file
        out_file = video.download(output_path="./dl_files",skip_existing= True)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        # result of success
        print(video.title + " downloaded.")
        f.write(video.title.strip() + ".mp3\n")  
    f.close()




def main(argv):
    # create dl_files directory if it does not exists
    path = "dl_files"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
       print("The dl_files directory is created!")
    help_string = """\nMore details:\n --mode  single or playlist \n --url specify youtube URL \n --mp3 Download MP3 only. Input yes. \n example: app.py -m playlist -u <play_list_url> \n example: app.py -m single -u <video_url> --mp3 yes"""
    try:
        parser = argparse.ArgumentParser(description="Youtube Downloader")
        # Add an argument
        parser.add_argument('--mode', type=str, required=True, help='Enter "single" or "playlist" without the double quotes',choices=['single','playlist'])
        parser.add_argument('--url', type=str, required=True, help='Enter the video or playlist youtube full URL')
        parser.add_argument('--mp3', type=str,default=False,help='Enter the "yes" for download mp3 only',choices=['yes'])
        args = parser.parse_args()
    except:
        print(help_string)
        sys.exit(2)

    # set the proper mp3_only boolean values. Should have a better logic for specifying the filter, or getting the argument.
    if args.mp3 == "yes":
        mp3_only = True
    elif args.mp3 == False:
        mp3_only = False

    # check if mode is single or playlist
    if args.mode == "single":
        # input validation check if the link is a single video or not. Videos with list? will also be downloaded without the playlist
        if "watch?" in args.url:
            dl_single(args.url,mp3_only)
        else:
            print("Video URL may not be a single video. Try again.")
            print(help_string)
            sys.exit(2)
    elif args.mode == "playlist":
        # input validation check if the link is a base playlist link.
        if "playlist?" in args.url:
            dl_playlist(args.url,mp3_only)
        else:
            print("Video URL may not be a Playlist. Try again.")
            print(help_string)
            sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])