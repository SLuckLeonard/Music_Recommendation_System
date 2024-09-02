import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
data = pd.read_csv(r'data\lastfm.csv')

# One-hot encode the 'best tag' feature
one_hot_tags = pd.get_dummies(data['best tag'], prefix='tag')

# Normalize numerical features
scaler = StandardScaler()
data[['listeners', 'plays', 'years']] = scaler.fit_transform(data[['listeners', 'plays', 'years']])

# Combine one-hot encoded tags with normalized features
features = pd.concat([data[['listeners', 'plays', 'years']], one_hot_tags], axis=1)

# Increased weight for tag for better recommendations
tag_weight = 2
features[one_hot_tags.columns] *= tag_weight

# Calculate cosine similarity
similarity_matrix = cosine_similarity(features)

# Function to get recommendations
def recommend_artists(artist_name, n_recommendations=10):
    artist_index = data[data['artist'] == artist_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[artist_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [i[0] for i in similarity_scores[1:n_recommendations+1]]
    return data['artist'].iloc[recommended_indices]


