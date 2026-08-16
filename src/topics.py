import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


class TopicAnalyzer:

    def __init__(self, number_of_topics=5, keywords_per_topic=8):
        self.number_of_topics = number_of_topics
        self.keywords_per_topic = keywords_per_topic
        self.vectorizer = None
        self.model = None

    def analyze(self, texts):

        texts = [
            str(text).strip()
            for text in texts
            if str(text).strip()
        ]

        if not texts:
            return pd.DataFrame(
                columns=["topic", "keyword", "weight"]
            )

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=3000,
            min_df=1
        )

        matrix = self.vectorizer.fit_transform(texts)

        topic_count = min(
            self.number_of_topics,
            matrix.shape[0],
            matrix.shape[1]
        )

        if topic_count < 1:
            return pd.DataFrame(
                columns=["topic", "keyword", "weight"]
            )

        self.model = NMF(
            n_components=topic_count,
            random_state=42,
            init="nndsvda",
            max_iter=500
        )

        self.model.fit(matrix)

        words = self.vectorizer.get_feature_names_out()

        results = []

        for topic_number, component in enumerate(
            self.model.components_,
            start=1
        ):

            top_indexes = component.argsort()[
                -self.keywords_per_topic:
            ][::-1]

            for index in top_indexes:
                results.append({
                    "topic": f"Topic {topic_number}",
                    "keyword": words[index],
                    "weight": round(
                        float(component[index]),
                        4
                    )
                })

        return pd.DataFrame(results)

    def get_summary(self, topic_df):

        if topic_df.empty:
            return pd.DataFrame(
                columns=["topic", "keywords"]
            )

        summary = (
            topic_df
            .groupby("topic")["keyword"]
            .apply(lambda words: ", ".join(words))
            .reset_index()
        )

        summary.columns = [
            "topic",
            "keywords"
        ]

        return summary

    def save_results(self, topic_df, output_path):

        topic_df.to_csv(
            output_path,
            index=False
        )

        return output_path