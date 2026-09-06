import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


st.set_page_config(
    page_title="Movie Sentiment Analyzer",
    layout="wide"
)

st.title("FILM PULSE: Sentiment Analysis of Movie Reviews")
st.write("Analyze movie reviews and explore sentiment patterns in the dataset.")


def classify_sentiment(review):
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return polarity, sentiment


@st.cache_data
def load_data():
    try:
        df = pd.read_csv("reviews.csv")

        if "Review" not in df.columns:
            st.error("The CSV file must contain a column named 'Review'.")
            return pd.DataFrame()

    except FileNotFoundError:
        # Sample data used only when reviews.csv is not available
        sample_reviews = [
            "An absolute masterpiece. The directing and acting were top notch.",
            "A complete and utter waste of two hours. I wanted to leave.",
            "It was a decent film, but the ending felt rushed and unsatisfying.",
            "The visuals were stunningly beautiful, unlike anything I've seen.",
            "The plot was full of holes and made absolutely no sense at all.",
            "Highly recommended for a family movie night.",
            "A brilliant psychological thriller with a great soundtrack.",
            "The cringeworthy script ruined the entire movie. Avoid it.",
            "The main character was terrible and the pacing was slow.",
            "It felt stale and predictable, I almost fell asleep halfway.",
            "The performances were excellent and the story was very engaging.",
            "I expected much more from this movie.",
            "The film was okay but nothing particularly memorable.",
            "A wonderful story with strong emotional moments.",
            "The movie dragged on for too long.",
            "Great direction, great acting and beautiful cinematography.",
            "The story was confusing and difficult to follow.",
            "It was entertaining enough for a weekend watch.",
            "One of the best movies I have watched this year.",
            "The dialogue felt unnatural and poorly written."
        ]

        df = pd.DataFrame({"Review": sample_reviews})

    df = df.dropna(subset=["Review"]).copy()

    df["Polarity"] = df["Review"].apply(
        lambda review: TextBlob(str(review)).sentiment.polarity
    )

    df["Sentiment"] = df["Polarity"].apply(
        lambda polarity:
        "Positive" if polarity > 0.1
        else "Negative" if polarity < -0.1
        else "Neutral"
    )

    return df


tab1, tab2 = st.tabs(
    ["Test a Single Review", "Dataset Analytics"]
)


with tab1:
    st.header("Analyze a Movie Review")

    user_review = st.text_area(
        "Enter a movie review:",
        placeholder="Example: The movie was beautifully directed and the acting was excellent."
    )

    if st.button("Classify Sentiment"):

        if user_review.strip():

            polarity, sentiment = classify_sentiment(user_review)

            st.write(f"Polarity Score: **{polarity:.4f}**")

            if sentiment == "Positive":
                st.success("Sentiment: Positive")

            elif sentiment == "Negative":
                st.error("Sentiment: Negative")

            else:
                st.info("Sentiment: Neutral")

        else:
            st.warning("Please enter a movie review.")


with tab2:

    st.header("Movie Review Dataset")

    df = load_data()

    if not df.empty:

        st.subheader("Reviews")

        st.dataframe(
            df,
            use_container_width=True,
            height=450
        )

        st.subheader("Sentiment Summary")

        sentiment_counts = (
            df["Sentiment"]
            .value_counts()
            .reindex(
                ["Positive", "Neutral", "Negative"],
                fill_value=0
            )
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Positive Reviews",
            sentiment_counts["Positive"]
        )

        col2.metric(
            "Neutral Reviews",
            sentiment_counts["Neutral"]
        )

        col3.metric(
            "Negative Reviews",
            sentiment_counts["Negative"]
        )


        st.subheader("Sentiment Distribution")

        fig, ax = plt.subplots(figsize=(7, 4))

        sentiment_counts.plot(
            kind="bar",
            ax=ax,
            rot=0
        )

        ax.set_title("Sentiment Analysis of Movie Reviews")
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Number of Reviews")

        plt.tight_layout()

        st.pyplot(fig)


        st.subheader("Common Words in Reviews")

        positive_reviews = df[
            df["Sentiment"] == "Positive"
        ]["Review"]

        negative_reviews = df[
            df["Sentiment"] == "Negative"
        ]["Review"]

        positive_text = " ".join(
            positive_reviews.astype(str)
        )

        negative_text = " ".join(
            negative_reviews.astype(str)
        )

        col4, col5 = st.columns(2)


        with col4:

            st.write("Positive Reviews")

            if positive_text.strip():

                positive_cloud = WordCloud(
                    width=600,
                    height=350,
                    background_color="white"
                ).generate(positive_text)

                fig_positive, ax_positive = plt.subplots()

                ax_positive.imshow(
                    positive_cloud,
                    interpolation="bilinear"
                )

                ax_positive.axis("off")

                st.pyplot(fig_positive)

            else:
                st.info("No positive reviews found.")


        with col5:

            st.write("Negative Reviews")

            if negative_text.strip():

                negative_cloud = WordCloud(
                    width=600,
                    height=350,
                    background_color="white"
                ).generate(negative_text)

                fig_negative, ax_negative = plt.subplots()

                ax_negative.imshow(
                    negative_cloud,
                    interpolation="bilinear"
                )

                ax_negative.axis("off")

                st.pyplot(fig_negative)

            else:
                st.info("No negative reviews found.")