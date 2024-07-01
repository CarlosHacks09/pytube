from pytube import YouTube

# URL of the YouTube video to download
video_url = 'https://www.youtube.com/watch?v=example'

# Create a YouTube object with the URL
yt = YouTube(video_url)

# Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory
stream.download()