# 📚 Book Recommendation System

This Book Recommendation System uses machine learning to provide personalized book recommendations based on user ratings and popular choices. The system leverages collaborative filtering and popularity-based models to offer accurate suggestions.

## 🔑 Key Features
- **Collaborative Filtering:** Personalized recommendations based on user preferences and book ratings.
- **Popularity-Based Recommendations:** Suggests books that are widely popular among the user base.
- **Pickle Storage for Models:** The recommendation models are saved using pickle files for efficient deployment.
- **Scalability:** Can be expanded with more datasets and enhanced algorithms.

## 🛠️ Project Structure
- **`book-recommender.ipynb`**: Jupyter notebook containing the core recommendation logic.
- **`app.py`**: Python script to run the web application.
- **`models/`**: Directory containing pickle files for models like `popular.pkl` and `similarity_score.pkl`.
- **`data/`**: Contains CSV files such as:
  - `Books.csv`: Contains book metadata like title, author, and genre.
  - `Ratings.csv`: User ratings data for various books.
  - `Users.csv`: Demographics and other user data.

## 📂 Datasets
The datasets used are:
- **Books**: Metadata of books like title, author, and category.
- **Ratings**: User-book interaction and ratings (1-5 stars).
- **Users**: Basic user data that helps personalize recommendations.

## 🔍 How the System Works
1. **Data Preprocessing**: Data cleaning and transformation to prepare user-item matrices.
2. **Model Training**: Two models are implemented:
   - **Collaborative Filtering**: Uses a user-item matrix to compute user similarities and recommend books based on shared preferences.
   - **Popularity-Based Model**: Suggests top books based on their overall popularity.
3. **Pickle Model**: Once trained, the model is serialized into `.pkl` files for easy reuse.
4. **Web App Deployment**: The system is deployed as a web application using `app.py`.

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- Necessary Python libraries (listed in `requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anirudhxchaturvedi/Book-Recommendation-System-
