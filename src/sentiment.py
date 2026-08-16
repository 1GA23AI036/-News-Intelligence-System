import pandas as pd
from textblob import TextBlob


class SentimentAnalyzer:

    def __init__(self):
        self.results = []

    def analyze_text(self, text):

        if pd.isna(text) or not str(text).strip():
            return {
                "sentiment": "Neutral",
                "polarity": 0.0,
                "subjectivity": 0.0
            }

        analysis = TextBlob(str(text))

        polarity = round(
            analysis.sentiment.polarity,
            4
        )

        subjectivity = round(
            analysis.sentiment.subjectivity,
            4
        )

        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return {
            "sentiment": sentiment,
            "polarity": polarity,
            "subjectivity": subjectivity
        }

    def analyze_articles(self, texts):

        results = []

        for article_id, text in enumerate(
            texts,
            start=1
        ):

            result = self.analyze_text(text)
            result["article_id"] = article_id
            results.append(result)

        self.results = results

        return pd.DataFrame(
            results,
            columns=[
                "article_id",
                "sentiment",
                "polarity",
                "subjectivity"
            ]
        )

    def get_summary(self, sentiment_df):

        if sentiment_df.empty:
            return pd.DataFrame(
                columns=["sentiment", "count"]
            )

        summary = (
            sentiment_df["sentiment"]
            .value_counts()
            .reset_index()
        )

        summary.columns = [
            "sentiment",
            "count"
        ]

        return summary

    def save_results(
        self,
        sentiment_df,
        output_path
    ):

        sentiment_df.to_csv(
            output_path,
            index=False
        )

        return output_path