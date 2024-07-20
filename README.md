# Movie Recommender System
this is one of my  failed project the tmdb api is not working somehow i have spent 3 days finding the alternative for api but here is a sample that how this project should look like 

https://github.com/user-attachments/assets/c1d80429-f643-4e2f-b8f5-b059800c9c9a

 ## Overview
 but my project look like this without the poster api
 
https://github.com/user-attachments/assets/e722fb74-5b78-472d-9afb-a6c3dcaca941

This project aims to create a movie recommendation system using collaborative filtering and content-based filtering techniques. The recommender system suggests movies to users based on their preferences and past interactions.

## Project Structure
- `movie_recomdation.ipynb`: Jupyter Notebook with data analysis, preprocessing, model training, and evaluation.
- `app.py`: Streamlit app for user interaction, allowing users to input movie preferences and get recommendations.
- `requirements.txt`: Dependencies required to run the project.

## Steps Performed

### 1. Data Collection
- Imported datasets from a movie database.
- Merged and cleaned the datasets for analysis.

### 2. Data Preprocessing
- Handled missing values and inconsistencies.
- Performed data normalization and scaling.

### 3. Feature Engineering
- Extracted relevant features such as genres, ratings, and user interactions.

### 4. Model Training
- Implemented collaborative filtering using matrix factorization.
- Built content-based filtering using movie metadata.
- Trained models on the preprocessed data.

### 5. Model Evaluation
- Evaluated model performance using metrics like RMSE and precision.
- Fine-tuned hyperparameters for optimal performance.

### 6. Deployment
- Developed a Streamlit app (`app.py`) for user-friendly interaction.
- Users can input their preferences and receive movie recommendations.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shubh123a3/movie-recommender-system.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- Integrate real-time user feedback for improving recommendations.
- Expand the dataset to include more movies and user interactions.
- Implement a hybrid recommendation system combining collaborative and content-based filtering.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

Check out the repository and share your feedback: [Movie Recommender System](https://github.com/shubh123a3/movie-recommender-system)
