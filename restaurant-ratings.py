# # your code goes here
# Reads the ratings in from the file
# Stores them in a dictionary, and then
# Spits out the ratings in alphabetical order by restaurant


def read_ratings(filename):
    """Given the name of a ratings file as input, returns a dictionary whose
    entries are of the form name: rating.
    """

    log_file = open(filename)
    ratings = {}
    for line in log_file:
        # could also use str slices after .rstrip: ratings[text[:-2]] = text[-1]
        restaurant, score = line.rstrip().split(":")
        #assigning the key(restaurant)to the value(score)
        ratings[restaurant] = score

    log_file.close()
    return ratings

ratings = read_ratings("scores.txt")

alpha_ratings = sorted(ratings.items())

for restaurant, rating in alpha_ratings:
    # print restaurant + " is rated at " + rating + "."
    print "{restaurant} is rated at {rating}.".format(restaurant=restaurant,
                                                      rating=rating)
