📚 Book Recommendation System

A web-based book recommendation app built using **Flask** and **machine learning**. It suggests books similar to the one entered by the user using cosine similarity on user ratings. The app also showcases the most popular books on the homepage.

---

## 🌟 Features

- ✅ Content-based filtering using cosine similarity
- ✅ Top 50 most popular books on homepage
- ✅ Search any book and get 4 similar recommendations
- ✅ Simple and responsive UI using Bootstrap
- ✅ Fast performance using preprocessed pickle files

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Data**: Pandas, NumPy, Scikit-learn
- **Frontend**: HTML, CSS, Bootstrap
- **Model Storage**: Pickle

---

## 🧠 How It Works

- The system creates a **pivot table** with Book Titles vs User IDs and their ratings.
- **Cosine similarity** is calculated between all book vectors.
- When a user searches for a book, the system retrieves the top 4 most similar books based on similarity scores.
- All recommendations and top-rated books are displayed with their title, author, and cover image.

---

## 🎥 Screen Recording

> Watch a quick demo of the Book Recommendation System in action:

- [📺 Click here to view the screen recording of Source Code](https://youtu.be/rgZmddvGSII)
- [📺 Click here to view the screen recording of Code In Action](https://youtu.be/broam-NQRK4)

---

## 💡 Future Improvements

- 🔍 Add fuzzy search or autocomplete for better input matching
- 🧠 Integrate collaborative filtering (matrix factorization)
- ☁️ Deploy on Render or PythonAnywhere
- 📱 Make the UI more mobile-responsive

---

## 🧑‍💻 Author

Atharv Singh  
[LinkedIn](https://www.linkedin.com/in/itsbabuaa) • [GitHub](https://github.com/itsbabuaa)

---

## 📄 License

This project is open source.

