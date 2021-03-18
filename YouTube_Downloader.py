import pytube
from pytube import YouTube
print('You have to restart everytime you want to download a Video!')

# Get Video URL and get Video from YouTube
video_url = input('Video URL: ')
youtube = pytube.YouTube(video_url)
# selects highest resolution of the video to download
video = youtube.streams.get_highest_resolution()
#download video
video.download()
print('Download Finished')
print('You will find the downloaded in the same folder as the .exe or .py')

# script to stop the programm
determinate = input('Press any key to terminate the program')
terminate = 'Bye Bye'
print(terminate)
