from pytube import YouTube
url=input("Enter YouTube URL:")
YouTube(url).streams.first().download(r'Downloads')