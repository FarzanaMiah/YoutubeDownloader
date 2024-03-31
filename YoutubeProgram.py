from pytube import YouTube
import os

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # Specify the directory where you want to save the video
    download_directory = "downloads"

    # Create the directory if it doesn't exist
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    # Download the video to the specified directory
    yd.download(output_path=download_directory)

    print("Download complete. Video saved in the '{}' folder.".format(download_directory))
except Exception as e:
    print("An error occurred:", str(e))
