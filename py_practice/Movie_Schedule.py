# Creating Movie schedule using dictionaries
current_movies = {'Rouge one': '4:50PM',
                  'Joker': '6:00PM',
                  'Stalin': '3:00AM'
                  }
print("List of current movies:\n")
for key in current_movies:
    print(key)

movie = input("Which movie timings would you like to know?\n")
showtime = current_movies.get(movie)
if showtime is None:
    print("Requested showtime isn't playing")
else:
    print("Requested showtime playing at", current_movies.get(movie), sep=' ')




