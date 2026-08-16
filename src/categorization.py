import pandas as pd


class NewsCategorizer:

    def __init__(self):
        self.categories = {
            "Politics": [
                "government", "president", "minister",
                "election", "parliament", "politics",
                "party", "vote", "policy"
            ],
            "Business": [
                "business", "economy", "company",
                "market", "bank", "finance",
                "investment", "trade", "money"
            ],
            "Sports": [
                "football", "basketball", "sports",
                "player", "team", "match",
                "league", "goal", "championship"
            ],
            "Technology": [
                "technology", "software", "computer",
                "artificial", "intelligence", "digital",
                "internet", "cyber", "technology"
            ],
            "Health": [
                "health", "hospital", "doctor",
                "medicine", "disease", "medical",
                "patient", "virus", "treatment"
            ],
            "World": [
                "international", "world", "country",
                "war", "global", "foreign",
                "president", "nation"
            ],
            "Entertainment": [
                "movie", "music", "actor",
                "actress", "film", "celebrity",
                "concert", "television", "show"
            ]
        }

    def categorize_text(self, text):

        text = str(text).lower()

        scores = {}

        for category, keywords in self.categories.items():

            score = 0

            for keyword in keywords:
                if keyword in text:
                    score += 1

            scores[category] = score

        best_category = max(
            scores,
            key=scores.get
        )

        if scores[best_category] == 0:
            return "General"

        return best_category

    def categorize(self, texts):

        results = []

        for article_id, text in enumerate(
            texts,
            start=1
        ):

            category = self.categorize_text(text)

            results.append({
                "article_id": article_id,
                "category": category
            })

        return pd.DataFrame(results)

    def get_summary(self, category_df):

        if category_df.empty:
            return pd.DataFrame(
                columns=[
                    "category",
                    "count"
                ]
            )

        summary = (
            category_df["category"]
            .value_counts()
            .reset_index()
        )

        summary.columns = [
            "category",
            "count"
        ]

        return summary

    def save_results(
        self,
        category_df,
        output_path
    ):

        category_df.to_csv(
            output_path,
            index=False
        )

        return output_path