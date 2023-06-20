import pytube
import os

def create_videos_folder():
    if not os.path.exists('videos'):
        os.mkdir('videos')

def download_video(link):
    try:
        yt = pytube.YouTube(link)
        stream = yt.streams.get_highest_resolution()
        if stream:
            stream.download(output_path='videos')
            print("Downloaded:", link)
        else:
            print("No suitable stream found for:", link)
    except pytube.exceptions.PytubeError as e:
        print("Error downloading:", link)
        print(e)

def process_playlist(url):
    try:
        playlist = pytube.Playlist(url)
        create_videos_folder()

        for video in playlist.videos:
            download_video(video.watch_url)

        print("Download process complete.")
    except pytube.exceptions.PytubeError as e:
        print("Error processing the playlist:", e)

url = input("Please enter the YouTube playlist URL: ")

if url:
    process_playlist(url)
else:
    print("No URL provided.")
