import webbrowser
import os


# A utility function to retrieve file contents.
def file_get_contents(file_path):
    file = open(file_path)
    file_contents = file.read()
    file.close()
    return file_contents


# A utility function to create HTML content of the movie_container section of the page.
def create_movie_container_content(movies):
    movie_container_content = ''
    movie_template_content = file_get_contents("resources/html/movie_template.html")
    for movie in movies:
        # Append the movie information in the movie_template_content and add it to the movie_container_content.
        movie_container_content += movie_template_content.format(
            movie_title=movie.title,
            movie_story_line=movie.storyline,
            movie_poster=movie.poster,
            movie_trailer_youtube_id=movie.generate_trailer_youtube_id()
        )
    return movie_container_content


def open_movies_page(movies):
    # Create or overwrite the index.html file.
    index_html_file = open('index.html', 'w')

    # Get the template content designed for the index.html.
    index_template_content = file_get_contents("resources/html/index_template.html")

    # Add the dynamically generated html content of the movies to our index_template_content.
    index_html_content = index_template_content.format(movie_container=create_movie_container_content(movies))

    # Write generated content to the index.html file.
    index_html_file.write(index_html_content)
    # Close the file so that other processes can use it.
    index_html_file.close()

    # Open the index.html file in a browser by getting its absolute path in the system and using
    # file protocol to open it.
    url = os.path.abspath(index_html_file.name)
    # new parameter having value 2 specifies that a New Tab should be created if possible.
    webbrowser.open('file://' + url, new=2)
