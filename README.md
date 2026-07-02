# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python, Pandas, Scikit-learn, and Streamlit**. This application recommends similar movies based on the movie selected by the user using **CountVectorizer** and **Cosine Similarity**.

---

## 🚀 Features

- 🎥 Recommend Top 5 Similar Movies
- 🔍 Content-Based Recommendation
- 📊 Cosine Similarity Algorithm
- 💻 Interactive Streamlit User Interface
- ⚡ Fast Recommendation System
- 📂 Easy to Use

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│── app.py
│── app_ui.py
│── model.py
│── movies.pkl
│── similarity.pkl
│── tmdb_5000_movies.csv
│── tmdb_5000_credits.csv
│── requirements.txt
│── README.md
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**.

Dataset includes:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

### Go to Project Folder

```bash
cd Movie-Recommendation-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Model Files

```bash
python model.py
```

### Run Streamlit App

```bash
streamlit run app_ui.py
```

---

## 🧠 How It Works

1. Load TMDB Movie Dataset.
2. Merge Movie and Credits datasets.
3. Perform Data Preprocessing.
4. Create Tags using:
   - Overview
   - Genres
   - Keywords
   - Cast
   - Director
5. Apply CountVectorizer.
6. Calculate Cosine Similarity.
7. Recommend Top 5 Most Similar Movies.

---

## 📷 Demo

Select your favorite movie and the application recommends five similar movies instantly using Content-Based Filtering.

---

## 📈 Future Improvements

- Add Movie Posters
- Add Movie Ratings
- Add Release Date
- Search Suggestions
- Deploy on Streamlit Cloud
- Improve UI Design

---

## 👩‍💻 Author

**Priyanshi Kumari**

- GitHub: https://github.com/priyanshiKumari197
- LinkedIn: https://www.linkedin.com/in/priyanshi197/

---

⭐ If you like this project, don't forget to give it a star!
