import os
import matplotlib.pyplot as plt


class NewsVisualizer:

    def __init__(self, output_folder="output"):
        self.output_folder = output_folder
        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    def save_chart(self, filename):
        path = os.path.join(
            self.output_folder,
            filename
        )

        plt.tight_layout()
        plt.savefig(
            path,
            dpi=150,
            bbox_inches="tight"
        )
        plt.close()

        return path

    def sentiment_chart(self, sentiment_df):

        if sentiment_df.empty:
            return None

        counts = (
            sentiment_df["sentiment"]
            .value_counts()
        )

        plt.figure(figsize=(8, 5))

        counts.plot(
            kind="bar"
        )

        plt.title("News Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Number of Articles")

        return self.save_chart(
            "sentiment_distribution.png"
        )

    def category_chart(self, category_df):

        if category_df.empty:
            return None

        counts = (
            category_df["category"]
            .value_counts()
        )

        plt.figure(figsize=(9, 5))

        counts.plot(
            kind="bar"
        )

        plt.title("News Category Distribution")
        plt.xlabel("Category")
        plt.ylabel("Number of Articles")

        return self.save_chart(
            "category_distribution.png"
        )

    def entity_chart(self, entity_df):

        if entity_df.empty:
            return None

        counts = (
            entity_df["entity"]
            .value_counts()
            .head(15)
        )

        plt.figure(figsize=(10, 6))

        counts.sort_values().plot(
            kind="barh"
        )

        plt.title("Top Named Entities")
        plt.xlabel("Occurrences")
        plt.ylabel("Entity")

        return self.save_chart(
            "top_entities.png"
        )

    def keyword_chart(self, keyword_df):

        if keyword_df.empty:
            return None

        data = keyword_df.head(15)

        plt.figure(figsize=(10, 6))

        plt.barh(
            data["keyword"],
            data["score"]
        )

        plt.title("Important News Keywords")
        plt.xlabel("TF-IDF Score")
        plt.ylabel("Keyword")

        return self.save_chart(
            "top_keywords.png"
        )