from collections import defaultdict

# Updated sample data: user ratings for a wider range of movies
user_ratings = {
    'User1': {'The Matrix': 5, 'Titanic': 1, 'Die Hard': 4, 'Barbie': 2, 'The Devil Wears Prada': 3, 'Final Destination': 3},
    'User2': {'The Matrix': 3, 'Titanic': 5, 'Die Hard': 2, 'Barbie': 4, 'Amazon': 4, 'Interstellar': 5},
    'User3': {'The Matrix': 2, 'Titanic': 5, 'Die Hard': 3, 'Final Destination': 4, 'Pirates of the Caribbean': 3, 'Interstellar': 4},
    'User4': {'The Matrix': 3, 'Titanic': 4, 'Die Hard': 5, 'The Devil Wears Prada': 5, 'Amazon': 3, 'Barbie': 1},
}

# Expanded movie genres
movie_genres = {
    'The Matrix': ['Action', 'Sci-Fi'],
    'Titanic': ['Drama', 'Romance'],
    'Die Hard': ['Action', 'Thriller'],
    'Barbie': ['Family', 'Animation'],
    'The Devil Wears Prada': ['Comedy', 'Drama'],
    'Final Destination': ['Horror', 'Thriller'],
    'Amazon': ['Documentary', 'Adventure'],
    'Interstellar': ['Sci-Fi', 'Drama'],
    'Pirates of the Caribbean': ['Adventure', 'Fantasy'],
}

# Collaborative Filtering
def compute_similarity(user1, user2):
    common_movies = set(user_ratings[user1]) & set(user_ratings[user2])
    if not common_movies:
        return 0
    ratings_diff_sq = sum((user_ratings[user1][movie] - user_ratings[user2][movie]) ** 2 for movie in common_movies)
    return 1 / (1 + ratings_diff_sq)

def recommend_movies_collab(user):
    scores = [(compute_similarity(user, other), other) for other in user_ratings if other != user]
    scores.sort(reverse=True)
    top_match = scores[0][1]
    recommendations = [movie for movie in user_ratings[top_match] if movie not in user_ratings[user]]
    return recommendations

# Content-Based Filtering
def get_favorite_genre(user):
    genre_count = defaultdict(int)
    for movie, rating in user_ratings[user].items():
        if rating >= 4:
            for genre in movie_genres[movie]:
                genre_count[genre] += 1
    return max(genre_count, key=genre_count.get) if genre_count else None

def recommend_movies_content(user):
    favorite_genre = get_favorite_genre(user)
    recommendations = [movie for movie, genres in movie_genres.items() if favorite_genre in genres and movie not in user_ratings[user]]
    return recommendations

# Combining Collaborative and Content-Based Recommendations
def recommend_movies(user):
    collab_recommendations = recommend_movies_collab(user)
    content_recommendations = recommend_movies_content(user)
    combined_recommendations = set(collab_recommendations + content_recommendations)
    return combined_recommendations

# Example Usage
user = 'User1'
print(f"Recommendations for {user}: {recommend_movies(user)}")
