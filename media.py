import webbrowser
import re


class Movie:
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        # Opens the Web Browser with the trailer URL of the movie.
        webbrowser.open(self.trailer)

    def generate_trailer_youtube_id(self):
        # Extract the YouTube ID from the trailer URL of the movie.
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', self.trailer)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        return trailer_youtube_id
