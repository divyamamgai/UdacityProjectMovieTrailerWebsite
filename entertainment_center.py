import fresh_tomatoes
import media

# Initialize all the movies.
movies = [
    media.Movie(
        "Cars",
        "Lightning McQueen, a racing car, learns a hard lesson in life when he damages a lot of property in "
        "Radiator Springs. His task is to repair the damage done before he can get back on the road.",
        "http://www.gstatic.com/tv/thumb/movieposters/159400/p159400_p_v8_aa.jpg",
        "https://www.youtube.com/watch?v=SbXIj2T-_uk"),
    media.Movie(
        "WALL-E",
        "A robot who is responsible for cleaning a waste-covered Earth meets another robot and falls in love with her. "
        "Together, they set out on a journey that will alter the fate of mankind.",
        "http://www.gstatic.com/tv/thumb/movieposters/174374/p174374_p_v8_ab.jpg",
        "https://www.youtube.com/watch?v=alIq_wG9FNk"),
    media.Movie(
        "Finding Nemo",
        "After his son gets abducted in the Great Barrier Reef and is despatched to Sydney, a meek clownfish "
        "embarks on a journey to bring him home.",
        "http://www.impawards.com/2003/posters/finding_nemo.jpg",
        "https://www.youtube.com/watch?v=wZdpNglLbt8"),
    media.Movie(
        "Monsters, Inc.",
        "Top scarer Sulley and his friend Mike are scared silly when a little girl wanders into Monstropolis, "
        "their monster world, and try their best to get her back to her room.",
        "http://t2.gstatic.com/images?q=tbn:ANd9GcTaeFK9RkQM00A7cbfc2iI3C573rSkbsubdyrY-ZZnT4jk0O_cB",
        "https://www.youtube.com/watch?v=Ue_SfrHHBAc"),
    media.Movie(
        "Toy Story",
        "Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called "
        "Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz.",
        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc"),
    media.Movie(
        "The Incredibles",
        "Forced to adopt a civilian identity and stuck in a white-collar job, Mr. Incredible itches to get back "
        "into action. Soon, he is lured into a trap and now his family must contrive to save him.",
        "http://www.gstatic.com/tv/thumb/movieposters/35032/p35032_p_v8_aa.jpg",
        "https://www.youtube.com/watch?v=eZbzbC9285I")
]

# Create and Open the movies page.
fresh_tomatoes.open_movies_page(movies)
