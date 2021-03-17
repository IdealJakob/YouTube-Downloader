import pytube
from pytube import YouTube

video_url = input('Video URL: ')
youtube = pytube.YouTube(video_url)
video = youtube.streams.get_highest_resolution()
video.download()
print('Download Finished')

determinate = input('Press any key to terminate the program')
terminate = 'Bye Bye'
print(terminate)