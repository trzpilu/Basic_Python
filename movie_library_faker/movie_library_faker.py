from faker import Faker
from operator import itemgetter, attrgetter
from tabulate import tabulate

fake = Faker("pl_PL")

# CLASSES
# 1. Adding Class for Movies:
class Movie:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        
        #Variables
        self.plays = plays
    
    def play(self, step=1):
        self.plays += step

    def __str__(self):
        return f'{self.title, self.year, self.genre, self.plays}'
    
    def __repr__(self):
        return 'Movie(title: %s, year: %s, genre: %s, plays: %r)' % (self.title, self.year, self.genre, self.plays)
    
    def movie_details(self):
        return f"{self.title} ({self.year})"

    def isSeries(self):
        return False
    
    def to_list(self):
        return [self.title, self.year, self.genre, self.plays]
    
    
# 2. Adding Class for Series
class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        
    def series_details(self):
        return f"{self.title} S{self.season}E{self.episode}"
    
    def __repr__(self):
        return 'Series(title: %s, year: %s, genre: %s, plays: %r, episode: %r, season: %r)' % (self.title, self.year, self.genre, self.plays, self.episode, self.season)

    def play(self, step=1):
        self.plays += step

    def isSeries(self):
        return True

    def to_list(self):
        return [self.title, self.year, self.genre, self.plays, self.season, self.episode]

# FUNCTIONS
# 1. Generates movies and adds them to main_list. Returns appended main_list.
def generate_movies():
    for i in range(10):
        main_list.append(
            Movie(
                title = fake.name(),
                year = fake.year(),
                genre = fake.name(),
                plays = fake.random_int(0,100)
            )
        )
    return main_list    
# 2. Generates series and adds them to main list. Returns appended main_list.
def generate_series():
    
    for j in range(10):
        main_list.append(
            Series(
                title = fake.name(),
                year = fake.year(),
                genre = fake.name(),
                season = fake.random_int(1, 4),          
                episode = fake.random_int(0, 20),
                plays = fake.random_int(0, 100)
            )
        )
    return main_list

# 3. Runs generate_movies and generate_series, returnig main_list.
def generate_data():
    generate_movies()
    generate_series()   
    return main_list

# 4. Runs generate_views() importing the main_list, then 
#    runs Movie.play(). Returns main_list
def generate_views(main_list):
    for k in range(10):
        for l in main_list:
            Movie.play(l)
    return main_list

# 5. 1. get_movies takes the main_list, filters out only Class Movie() and
#    prints the resulting list in alphabetical order
    
def get_movies(main_list):
    movie_list = []
    for item in main_list:
        if item.isSeries() == False:
            movie_list.append(item)
    movie_list_by_title = sorted(movie_list, key=lambda item: item.title)
    movies_as_list = [m.to_list() for m in movie_list_by_title]
    print("-------------------------------------------------------")
    print("This is a list of your movies, sorted alphabetically:")
    print("-------------------------------------------------------")
    print(tabulate(movies_as_list, headers= ["Title", "Year", "Genre", "Plays"]))
  

# 5. 2. get_movies takes the main_list, filters out only Class Movie() and
#    prints the resulting list in alphabetical order    
def get_series(main_list):
    series_list = []
    for item in main_list:
        if item.isSeries() == True:
            series_list.append(item)
    series_list_by_title = sorted(series_list, key=lambda item: item.title)
    series_as_list = [n.to_list() for n in series_list_by_title]
    print("------------------------------------------------------")
    print("This is a list of your series, sorted alphabetically:")
    print("------------------------------------------------------")
    print(tabulate(series_as_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))

    

# 6. Searches main_list for title and prints movie located on the main_list

def search(main_list):
    print("-----------------------------------------------")
    print(" Please choose a title from the lists above.")
    print("-----------------------------------------------")
    search_result = []
    search_title = input("What title are you looking for? ")
    for item in main_list:
        if item.title == search_title:
            search_result.append(item)
            
            if item.isSeries() == False:
                search_as_list = [o.to_list() for o in search_result]
                print(tabulate(search_as_list, headers= ["Title", "Year", "Genre", "Plays"]))

            elif item.isSeries() == True:
                search_as_list = [o.to_list() for o in search_result]
                print(tabulate(search_as_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))


# 7. top_titels searches the top 'x' number of top titles. Takes 
#    variable 'x' from input and prints top_list.
def top_titles(main_list):
    print("Najpopularniejsze filmy i seriale dnia dzisiaj")
    x =  int(input("How many Top movies and series would you like to see? "))
    for item in main_list:
        by_plays = (sorted(main_list, key=lambda item: item.plays, reverse=True))
    
    top_list= by_plays[0:x]
    
    top_as_list = [p.to_list() for p in top_list]
    print("------------------------------------")
    print("Here is you list, sorted by views:")
    print("------------------------------------")
    print(tabulate(top_as_list, headers= ["Title", "Year", "Genre", "Plays", "Season", "Episode"]))
   


if __name__ == "__main__":
    main_list = []
    print("Biblioteka filmów")
    print("Generating movies and series data... please wait.")
    
    # Generate main_list:
    generate_data()
    #print(main_list)
    
    # Generate views for plays in main_list:
    generate_views(main_list) 
    #print(main_list)
    
    # Get Movie tuples from main_list and transfer to movie_list,
    # sorted alphabetically by title.
    get_movies(main_list)
    print()
    
    # Get Series tuples from main_list and transfer to series_list,
    # sorted alphabetically by title.
    get_series(main_list)
    print()
    
    # Search the list for title.
    search(main_list)
    print()

    # Return a requested number of top titles.
    top_titles(main_list)

