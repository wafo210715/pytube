from pytubefix import YouTube

yt_url = "https://www.youtube.com/watch?v=g4vcoY8X_1o"
yt = YouTube(yt_url)

# Print all available streams
print("Available streams:")
for stream in yt.streams.filter(progressive=True, file_extension="mp4"):
    print(f"Resolution: {stream.resolution}, FPS: {stream.fps}, Size: {stream.filesize / 1024 / 1024:.2f} MB")

# Get the highest resolution stream
stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

# Print information about the selected stream
print(f"\nSelected stream:")
print(f"Downloading: {stream.title}")
print(f"Resolution: {stream.resolution}")
print(f"File size: {stream.filesize / 1024 / 1024:.2f} MB")

# Download the video
print("Downloading...")
stream.download()
print("Download complete!")
