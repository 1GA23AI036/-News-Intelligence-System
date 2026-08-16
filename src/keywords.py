import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class KeywordExtractor:

    def __init__(self, max_keywords=20):
        self.max_keywords = max_keywords
        self.vectorizer = None

    def extract(self, texts):

        texts = [
            str(text).strip()
            for text in texts
            if str(text).strip()
        ]

        if not texts:
            return pd.DataFrame(
                columns=["keyword", "score"]
            )

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=3000
        )

        matrix = self.vectorizer.fit_transform(texts)

        scores = matrix.mean(axis=0).A1
        words = self.vectorizer.get_feature_names_out()

        results = pd.DataFrame({
            "keyword": words,
            "score": scores
        })

        results = results.sort_values(
            "score",
            ascending=False
        ).head(self.max_keywords)

        results["score"] = results["score"].round(4)

        return results.reset_index(drop=True)

    def save_results(self, keyword_df, output_path):

        keyword_df.to_csv(
            output_path,
            index=False
        )

        return output_path