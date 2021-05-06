import pytube
from pytube import YouTube
print('You have to restart everytime you want to download a Video!')
print('It has to be a YouTube-Video!')

# Get Video URL and get Video from YouTube
video_url = input('Video URL: ')
youtube = pytube.YouTube(video_url)

# selects highest resolution of the video to download
video = youtube.streams.get_highest_resolution()

# get path where to download this video to
print('Please write the Path to the Folder where you want this file in the next field!')
print('If you want it in the folder where this python file is leave blank.')
print('Paste from your clipboard with right click!')
path = input('Insert Folder Path here: ')

# Download video
video.download(path)
print('Download Finished')
print('You will find the downloaded Video in the same folder as the .exe or .py')

# script to stop the programm

determinate = input('Press any key to terminate the program')
terminate = 'Bye Bye'
print(terminate)
