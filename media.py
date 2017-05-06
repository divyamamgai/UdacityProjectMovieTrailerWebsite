import webbrowser
import re
import urllib.request
import urllib.parse
import json
# as keyword creates an alias for xml.etree.ElementTree as ET, so we can use ET to reference xml.etree.ElementTree.
import xml.etree.ElementTree as eT


class Movie:
    def __init__(self, title, plot, poster, trailer_url):
        self.title = title
        self.plot = plot
        self.poster_url = poster
        self.trailer_url = trailer_url

    def show_trailer(self):
        # Opens the Web Browser with the trailer URL of the movie.
        webbrowser.open(self.trailer_url)

    @staticmethod
    def generate_traileraddict_id(title):
        # Firstly strip the title to remove excess white spaces surrounding the text.
        # Secondly remove all the non-alphabet and non-numeric characters from the title.
        # Thirdly convert the result to lowercase and convert all the white spaces (even the groups) to dash.
        return re.sub(r"(\s|-)+", "-", (re.sub(r"[^a-zA-Z0-9\s\-]", "", title.strip())).lower())

    @staticmethod
    def initialize_from_title(title, traileraddict_trailer_type="trailer"):
        print("Requesting information for the movie '" + title + "' from omdb...")
        # Make API request to omdb to get movie information.
        omdb_api_connection = urllib.request.urlopen("http://www.omdbapi.com/?t=" + urllib.parse.quote(title))
        omdb_api_response = omdb_api_connection.read()
        omdb_api_connection.close()
        # http.client.HTTPResponse.read() returns raw bytes which is needed to be converted
        # to string using UTF-8 encoding.
        omdb_movie_data = json.loads(omdb_api_response.decode("utf-8"))
        # Check whether the movie was found or not.
        if omdb_movie_data["Response"] == "True":
            print("Movie information found successfully!")
            print("Requesting trailer for the movie '" + title + "' from Trailer Addict...")
            # Make API request to Trailer Addict to get movie trailer.
            traileraddict_api_connection = urllib.request.urlopen("http://simpleapi.traileraddict.com/" +
                                                                  Movie.generate_traileraddict_id(title) +
                                                                  "/" + traileraddict_trailer_type)
            traileraddict_api_response = traileraddict_api_connection.read()
            traileraddict_api_connection.close()
            # Parse XML returned as response from the Trailer Addict API.
            traileraddict_xml_root = eT.fromstring(traileraddict_api_response.decode("utf-8"))
            # In the Trailer Addict Simple API first element of the root is trailer which
            # contains the desired movie data. Inside that trailer element is an tag, embed_standard,
            # which contains embed HTML code for the trailer. We parse the embed HTML code to get
            # the movie trailer URL from the src attribute of the iframe element.
            trailer_url = eT.fromstring(traileraddict_xml_root[0].find("embed_standard").text).attrib["src"]
            print("Movie trailer found successfully!")
            movie = Movie(title, omdb_movie_data["Plot"], omdb_movie_data["Poster"], trailer_url)
            return movie
        else:
            print("Movie not found!")
            return None
