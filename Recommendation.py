movies = {
    "Inception": ["Sci-Fi", "Thriller", "Action"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Notebook": ["Romance", "Drama"],
    "La La Land": ["Romance", "Musical", "Drama"],
    "The Dark Knight": ["Action", "Thriller", "Crime"],
    "Toy Story": ["Animation", "Comedy", "Family"],
    "Finding Nemo": ["Animation", "Family", "Adventure"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Titanic": ["Romance", "Drama", "History"],
    "Coco": ["Animation", "Family", "Musical"],
}


def recommend_movies(liked_movie):
    liked_genres = movies[liked_movie]

    recommendations = []

    #
    for title, genres in movies.items():
        if title == liked_movie:
            continue

        match_count = 0
        for genre in genres:
            if genre in liked_genres:
                match_count += 1

        if match_count > 0:
            recommendations.append((title, match_count))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations


def main():
    print("Available movies:")
    for title in movies:
        print("-", title)

    while True:
        liked_movie = input("\nEnter a movie you like (or type 'quit' to stop): ")

        if liked_movie.lower() == "quit":
            print("Goodbye!")
            break

        matched_movie = None
        for title in movies:
            if title.lower() == liked_movie.lower():
                matched_movie = title
                break

        if matched_movie is None:
            print("Sorry, that movie is not in the list. Try again.")
            continue

        results = recommend_movies(matched_movie)

        print(f"\nBecause you liked '{matched_movie}', you might also like:")
        if not results:
            print("No similar movies found.")
        else:
            for title, score in results:
                print(f"- {title} ({score} matching genres)")


if __name__ == "__main__":
    main()
