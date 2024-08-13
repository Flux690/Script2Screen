import re
import requests
import math
from moviepy.editor import *

def download_and_save_videos(videos, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    current_dir = os.getcwd()
    video_clips = []
    
    for i, video in enumerate(videos):
        video_id = video.id
        download_url = f"https://www.pexels.com/video/{video_id}/download"
        
        response = requests.get(download_url)
        if response.status_code == 200:
            video_content = response.content
            video_file_path = os.path.join(current_dir, save_dir, f"sample_{i}.mp4")

            with open(video_file_path, "wb") as file:
                file.write(video_content)
                
            video_clip = VideoFileClip(video_file_path)
            video_clip = video_clip.resize((1280, 720)) # resize to 16:9 aspect ratio
            video_clips.append(video_clip)
    
    return video_clips

def combine_videos_and_add_subtitles(videos, text):
    # Load the audio clip
    audio_clip = AudioFileClip("speech.mp3")
    audio_duration = audio_clip.duration

    # Calculate the new duration for each video
    num_videos = len(videos)
    new_duration = math.ceil(audio_duration / num_videos)

    # Trim each video to the desired duration
    new_videos = []
    for i, video in enumerate(videos):
        if video.duration < new_duration:
            new_videos.append(video)
        else:
            end_time = new_duration
            trimmed_video = video.subclip(0, end_time)
            new_videos.append(trimmed_video)

    # Combine the trimmed videos into a single video
    combined_video = concatenate_videoclips(new_videos)

    # Create text clips for each sentence in the script
    script_sentences = text.split(". ")
    text_clips = []
    for i, sentence in enumerate(script_sentences):
        # # Check if any of the keywords are present in the sentence and apply bold styling
        # for keyword in keywords:
        #     bold_sentence = re.sub(fr'\b{keyword}\b', f'<b>{keyword}</b>', sentence, flags=re.IGNORECASE)
        #     sentence = bold_sentence

        text_clip = TextClip(sentence, font="Inter", fontsize=40, color="white", stroke_color="black", method="caption", stroke_width=0.3)
        # Calculate the start time and end time of the text clip based on the audio duration
        start_time = i * new_duration
        end_time = (i + 1) * new_duration
        text_clip = text_clip.set_start(start_time).set_end(end_time)
        text_clips.append(text_clip)

    # Combine the text clips with the video clip
    text_and_video = CompositeVideoClip([combined_video] + text_clips)

    # Set the audio file as the voiceover audio
    final_video = text_and_video.set_audio(audio_clip)

    # Save the combined video
    final_video.write_videofile("combined_video.mp4")

    return final_video