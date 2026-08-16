import os
import pandas as pd


class ReportGenerator:

    def __init__(self, output_folder="output"):
        self.output_folder = output_folder
        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    def save_csv(self, data, filename):

        path = os.path.join(
            self.output_folder,
            filename
        )

        if isinstance(data, dict):
            data = pd.DataFrame([data])

        data.to_csv(
            path,
            index=False
        )

        return path

    def save_all(
        self,
        cleaned_data=None,
        entities=None,
        topics=None,
        sentiment=None,
        keywords=None,
        categories=None,
        statistics=None
    ):

        files = {}

        if cleaned_data is not None:
            files["articles"] = self.save_csv(
                cleaned_data,
                "processed_articles.csv"
            )

        if entities is not None:
            files["entities"] = self.save_csv(
                entities,
                "entities.csv"
            )

        if topics is not None:
            files["topics"] = self.save_csv(
                topics,
                "topics.csv"
            )

        if sentiment is not None:
            files["sentiment"] = self.save_csv(
                sentiment,
                "sentiment.csv"
            )

        if keywords is not None:
            files["keywords"] = self.save_csv(
                keywords,
                "keywords.csv"
            )

        if categories is not None:
            files["categories"] = self.save_csv(
                categories,
                "categories.csv"
            )

        if statistics is not None:
            files["statistics"] = self.save_csv(
                statistics,
                "statistics.csv"
            )

        return files

    def create_summary(
        self,
        statistics,
        output_file="summary.txt"
    ):

        path = os.path.join(
            self.output_folder,
            output_file
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "NEWS INTELLIGENCE SYSTEM\n"
            )

            file.write(
                "=" * 40 + "\n\n"
            )

            for key, value in statistics.items():

                label = (
                    str(key)
                    .replace("_", " ")
                    .title()
                )

                file.write(
                    f"{label}: {value}\n"
                )

        return path