from pytube import YouTube
import os

def download_audio_from_youtube():
    url = input("Enter the YouTube URL: ")
    video = YouTube(url)
    
    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'
    
    song_name = input("Enter the song name: ")
    
    audio_stream = video.streams.filter(only_audio=True).first()
    
    if audio_stream:
        audio_stream.download(output_path=path, filename=song_name + ".mp4")
        
        video_file_path = os.path.join(path, f"{song_name}.mp4")
        audio_file_path = os.path.join(path, f"{song_name}.mp3")
        
        if os.path.exists(video_file_path):
            os.rename(video_file_path, audio_file_path) if os.name == 'nt' else os.system(f'mv "{video_file_path}" "{audio_file_path}"')
            print(f"Audio downloaded and converted successfully: {audio_file_path}")
        else:
            print("Failed to download the audio stream.")
    else:
        print("No audio streams available for the given URL.")

if __name__ == "__main__":
    download_audio_from_youtube()
