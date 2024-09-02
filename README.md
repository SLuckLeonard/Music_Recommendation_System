# Music_Recommendation_System
# Overview
The Music Recommendation System is a web application designed to recommend similar artists based on a given artist's name. Utilizing a content-based filtering approach, the system provides users with artist recommendations based on various features extracted from a dataset. This project demonstrates proficiency in Python, Flask, data manipulation, and web development.

# Features
1. <b>Artist Recommendations</b>: Provides a list of artists similar to the input artist based on content-based filtering.
2. <b>User-Friendly Web Interface</b>: A simple web interface built with Flask where users can input an artist name and receive recommendations.
3. <b>Error Handling</b>: Displays appropriate messages if the artist is not found in the dataset.
4. <b>Normalization</b>: Handles case-insensitive searches by normalizing capitalization in both user input and dataset.

# Technologies Used
- <b>Python</b>: Core programming language used for building the recommendation logic and backend.
- <b>Flask</b>: Web framework for creating the web application and handling user requests.
- <b>Pandas</b>: Data manipulation library used for loading and processing the dataset.
- <b>Scikit-Learn</b>: Library used for calculating cosine similarity between artists.

# Dataset
The dataset for this project is sourced from Kaggle. You can find the dataset at the following link:
- [Music Dataset on Kaggle](https://www.kaggle.com/datasets/hoandan/lastfm?resource=download)

# Installation
1. Clone the Repository:
```bash
git clone https://github.com/yourusername/music-recommendation-system.git
cd music-recommendation-system
```
2. Create and Activate a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Add Your Dataset:

Place your dataset CSV file in the project directory and update the path in app.py accordingly.

# Usage
1. Run the Application:

```bash
python app.py
```

2. Access the Web Interface:

Open your browser and go to http://127.0.0.1:5000/.

3. Enter an Artist Name:

Input an artist's name into the provided field.
Click "Get Recommendations" to see a list of similar artists.
# Project Structure
- <b>app.py</b>: Main Flask application file that sets up routes and handles requests.
  <p>&nbsp; </p>
- <b>music_recommender.py</b>: Contains the recommendation logic and functions for generating artist recommendations.
    <p>&nbsp; </p>
- <b>templates/</b>: Directory containing HTML templates.
    <p>&nbsp; </p>
- <b>index.html</b>: Homepage with a form for user input.
    <p>&nbsp; </p>
- <b>recommend.html</b>: Page displaying recommendations.
    <p>&nbsp; </p>
- <b>error.html</b>: Page showing an error message when an artist is not found.
    <p>&nbsp; </p>
- <b>requirements.txt</b>: List of Python dependencies for the project.
# Disclaimer
The dataset used contains only 1,240 artists. Some artists you search for may not be present in the dataset.

# Contributing
If you wish to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.
# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Contact
For questions or feedback, please contact me at samluckleonard@gmail.com