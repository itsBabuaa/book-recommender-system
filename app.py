from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load all the data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))

# Clean the pivot table index to ensure consistent comparison
pt.index = pt.index.map(str).str.strip().str.lower()

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           ratings=list(popular_df['avg_rating'].values),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '').strip().lower()

    # Debugging - print user input and sample index
    print("User input:", repr(user_input))
    print("Sample pt.index:", list(pt.index)[:5])

    matches = [i for i, title in enumerate(pt.index) if title == user_input]

    if not matches:
        return render_template('recommend.html', error="Book not found in database. Try another.", user_input=user_input)

    index = matches[0]
    distance = similarity_scores[index]
    similar_items = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        temp_title = pt.index[i[0]]
        temp_df = books[books['Book-Title'].str.lower().str.strip() == temp_title]
        temp_df = temp_df.drop_duplicates('Book-Title')

        if not temp_df.empty:
            item = [
                temp_df['Book-Title'].values[0],
                temp_df['Book-Author'].values[0],
                temp_df['Image-URL-M'].values[0]
            ]
            data.append(item)

    return render_template('recommend.html', recommendations=data, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)


# Babuaa