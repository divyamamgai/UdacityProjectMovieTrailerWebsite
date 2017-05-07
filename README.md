# Fresh Tomatoes

A movies trailer website buildable using Python which utilizes [OMDB](http://www.omdbapi.com/) and
[Trailer Addict](http://www.traileraddict.com/trailerapi) APIs.

### Dependencies

1. Python3 (Tested with Python 3.5.2)
2. Bash or CMD

##### Optional

1. PyCharm
  * YUI Compressor for JS and CSS

### How to build?

Run the following command -
```sh
$ python .\build.py
```

> **Note**: Internet connection is required to build the website by default since it uses OMDB and
> Trailer Addict APIs to retrieve movie details.

### How to run?

Open the `index.html` in the browser after you have completed the build process successfully.

### Where to modify the movies?

The movies being displayed on the website are initialized in the `entertainment_center.py` as the `media.Movie` objects.
You can modify the `movies` array of `media.Media` objects as per your wish.

### Demo

For a demo visit this link - [https://divyamamgai.github.io/UdacityProjectMovieTrailerWebsite/](https://divyamamgai.github.io/UdacityProjectMovieTrailerWebsite/)