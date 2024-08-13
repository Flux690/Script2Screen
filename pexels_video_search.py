# Set up Pexels API credentials
from pypexels import PyPexels

api_key = 'Paste your Pexels API Key here'
py_pexel = PyPexels(api_key=api_key)

def search_pexels_videos(keywords):
    video_entries = []
    for keyword in keywords:
        search_videos_page = py_pexel.videos_search(query=keyword, per_page=1, orientation='landscape')
        if search_videos_page.entries:
            video_entries.extend(search_videos_page.entries)
    return video_entries

def filter_landscape_videos(videos):
    landscape_videos = []
    for video in videos:
        if video.width >= video.height:
            landscape_videos.append(video)
    return landscape_videos