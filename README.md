# Python Youtube Downloader Demo | Tutorial
Author: DJENGINEER 2022

This tool is for educational purposes only.

# Files
There are 4 files.
- app.py: the main program
- 1 to 3 are snippets for you to look at if you want to build your own script.

# Usage

```bash
usage: app.py [-h] --mode {single,playlist} --url URL [--mp3 {yes}]

Youtube Downloader

optional arguments:
  -h, --help            show this help message and exit
  --mode {single,playlist}
                        Enter "single" or "playlist" without the double quotes
  --url URL             Enter the video or playlist youtube full URL
  --mp3 {yes}           Enter the "yes" for download mp3 only

More details:
 --mode  single or playlist 
 --url specify youtube URL 
 --mp3 Download MP3 only. Input yes. 
 example: app.py -m playlist -u <play_list_url> 
 example: app.py -m single -u <video_url> --mp3 yes
```

# References

```Python
# https://pytube.io/en/latest/api.html
# https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

# https://stackoverflow.com/questions/65683517/how-do-you-download-a-playlist-from-youtube-using-pytube

# argsparse
# https://docs.python.org/3/howto/argparse.html
# https://stackoverflow.com/questions/15836713/allowing-specific-values-for-an-argparse-argument
# https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
# https://stackoverflow.com/questions/28638813/how-to-make-a-short-and-long-version-of-a-required-argument-using-python-argpars
```