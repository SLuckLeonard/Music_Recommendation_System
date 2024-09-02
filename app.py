from flask import Flask, render_template, request
from music_recommender import recommend_artists  # Assuming the recommendation logic is in music_recommender.py
import pandas as pd

app = Flask(__name__)

# Load the dataset to use for checking artist names
data = pd.read_csv(r'data\lastfm.csv')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    artist_name = request.form['artist_name'].strip().lower()

    # Normalize capitalization in the dataset for comparison
    data['artist_normalized'] = data['artist'].str.strip().str.lower()

    if artist_name in data['artist_normalized'].values:
        # If artist exists, get recommendations
        artist_name_original = data[data['artist_normalized'] == artist_name]['artist'].iloc[0]
        recommendations = recommend_artists(artist_name_original)
        return render_template('recommend.html', recommendations=recommendations, artist_name=artist_name_original)
    else:
        # If artist does not exist, return an error message
        return render_template('error.html', artist_name=artist_name)


if __name__ == '__main__':
    app.run(debug=True)
