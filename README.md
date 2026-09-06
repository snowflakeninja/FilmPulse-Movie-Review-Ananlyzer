# Film Pulse - Movie Review Sentiment Analyzer

Film Pulse is a sentiment analysis web application built using Python and Streamlit. It analyzes movie reviews and classifies them as **Positive**, **Negative**, or **Neutral** based on their sentiment polarity.

The application also includes a dashboard for analyzing a dataset of movie reviews and visualizing sentiment patterns.

## Features

- Analyze a single movie review
- Calculate the sentiment polarity score
- Classify reviews as Positive, Negative, or Neutral
- Analyze a dataset of 50 movie reviews
- View sentiment distribution using a bar chart
- Generate word clouds for positive and negative reviews
- Interactive web interface using Streamlit

## Sentiment Classification

The project uses TextBlob to calculate the polarity score of each review.

The following thresholds are used:

| Polarity Score | Sentiment |
|---|---|
| Greater than 0.1 | Positive |
| Less than -0.1 | Negative |
| Between -0.1 and 0.1 | Neutral |

```python
if polarity > 0.1:
    sentiment = "Positive"
elif polarity < -0.1:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
```

## Technologies Used

- Python
- Streamlit
- Pandas
- TextBlob
- Matplotlib
- WordCloud

## Project Structure

```text
movie-sentiment-analyzer/
│
├── app.py
├── reviews.csv
├── requirements.txt
└── README.md
```

## Dataset

The project uses a CSV file containing 50 movie reviews.

The dataset contains a `Review` column. When the application runs, TextBlob calculates the polarity score for each review and assigns a sentiment category.

Example:

| Review | Polarity | Sentiment |
|---|---:|---|
| The movie was excellent and I enjoyed every minute of it. | 0.80 | Positive |
| The movie was terrible and painfully boring. | -0.70 | Negative |
| The film runs for two hours and is set in a coastal town. | 0.00 | Neutral |

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd movie-sentiment-analyzer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will start locally and can usually be accessed at:

```text
http://localhost:8501
```

## How It Works

1. The user enters a movie review.
2. TextBlob calculates the polarity of the review.
3. The polarity score is compared with the defined thresholds.
4. The review is classified as Positive, Negative, or Neutral.
5. For dataset analysis, reviews are loaded from `reviews.csv`.
6. Sentiment is calculated for each review.
7. Pandas is used to summarize the sentiment results.
8. Matplotlib is used to visualize the sentiment distribution.
9. WordCloud is used to display common words in positive and negative reviews.

## Future Improvements

- Train a machine learning model on a larger movie review dataset
- Add text preprocessing and cleaning
- Allow users to upload their own CSV datasets
- Compare different sentiment analysis techniques
- Add more sentiment visualizations
- Deploy the application online

