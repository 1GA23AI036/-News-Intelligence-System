import pandas as pd


class NewsAnalyzer:

    def __init__(self):
        self.data = None

    def generate_statistics(
        self,
        df,
        entities=None,
        topics=None,
        sentiment=None,
        keywords=None
    ):
        self.data = df.copy()

        statistics = {
            "total_articles": len(df),
            "total_columns": len(df.columns),
            "missing_values": int(
                df.isnull().sum().sum()
            )
        }

        text_column = None

        for column in [
            "text",
            "article",
            "content",
            "body",
            "clean_text"
        ]:
            if column in df.columns:
                text_column = column
                break

        if text_column:
            texts = (
                df[text_column]
                .fillna("")
                .astype(str)
            )

            statistics["total_words"] = int(
                texts.str.split().str.len().sum()
            )

            statistics["total_characters"] = int(
                texts.str.len().sum()
            )

        if entities is not None:
            statistics["total_entities"] = len(entities)

        if topics is not None:
            statistics["total_topic_records"] = len(topics)

        if sentiment is not None:
            statistics["positive_articles"] = int(
                (sentiment["sentiment"] == "Positive").sum()
            )

            statistics["negative_articles"] = int(
                (sentiment["sentiment"] == "Negative").sum()
            )

            statistics["neutral_articles"] = int(
                (sentiment["sentiment"] == "Neutral").sum()
            )

        if keywords is not None:
            statistics["total_keywords"] = len(keywords)

        return statistics

    def column_summary(self, df):

        results = []

        for column in df.columns:
            results.append({
                "column": column,
                "data_type": str(
                    df[column].dtype
                ),
                "missing_values": int(
                    df[column].isnull().sum()
                ),
                "unique_values": int(
                    df[column].nunique()
                )
            })

        return pd.DataFrame(results)

    def article_statistics(self, texts):

        results = []

        for article_id, text in enumerate(
            texts,
            start=1
        ):
            text = str(text)

            results.append({
                "article_id": article_id,
                "words": len(text.split()),
                "characters": len(text),
                "sentences": max(
                    1,
                    text.count(".")
                )
            })

        return pd.DataFrame(results)

    def save_results(self, data, output_path):

        if isinstance(data, dict):
            data = pd.DataFrame([data])

        data.to_csv(
            output_path,
            index=False
        )

        return output_path