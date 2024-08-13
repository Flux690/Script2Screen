from flask import Flask, render_template, request
from extract import extract_keywords
from text_to_speech import tts
from pexels_video_search import search_pexels_videos, filter_landscape_videos
from combine_videos import download_and_save_videos, combine_videos_and_add_subtitles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        voice = request.form["voice"]
        
        tts(text, voice)
        
        # Extract keywords from the text using DeepAI API
        keywords = extract_keywords(text)
        print(keywords[:5])

        # Search for videos using the extracted keywords
        videos = search_pexels_videos(keywords)
        landscape_videos = filter_landscape_videos(videos)
            
        if not landscape_videos:
            return "No landscape videos found for the given keywords."

        # Download and save videos as VideoFileClip objects
        video_clips = download_and_save_videos(landscape_videos, save_dir="video_clips")

        # Combine videos and add subtitles
        combine_videos_and_add_subtitles(video_clips, text)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)