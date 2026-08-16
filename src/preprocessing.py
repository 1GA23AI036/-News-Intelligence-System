import re
import pandas as pd


class NewsPreprocessor:

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None
        self.text_column = "content"

    def load_data(self, number_of_articles=None):
        """
        Load only the required number of rows.

        This is important because the full dataset is
        approximately 8.6 GB.
        """

        columns = [
            "content",
            "date",
            "title",
            "category",
            "author",
            "source",
            "fetched_at"
        ]

        self.data = pd.read_csv(
            self.dataset_path,
            usecols=columns,
            nrows=number_of_articles,
            low_memory=False
        )

        self.data["content"] = (
            self.data["content"]
            .fillna("")
            .astype(str)
        )

        self.data["title"] = (
            self.data["title"]
            .fillna("")
            .astype(str)
        )

        return self.data

    def find_text_column(self):
        """
        Return the newspaper article text column.
        """

        if self.data is None:
            self.load_data()

        return "content"

    def clean_text(self, text):
        """
        Clean newspaper article text.
        """

        text = str(text)

        text = re.sub(
            r"http\S+|www\S+",
            "",
            text
        )

        text = re.sub(
            r"\S+@\S+",
            "",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()

    def process(self):
        """
        Clean the article content and return
        the processed dataset.
        """

        if self.data is None:
            self.load_data()

        self.data["clean_text"] = (
            self.data["content"]
            .apply(self.clean_text)
        )

        return self.data

    def get_texts(self):
        """
        Return cleaned article texts as a list.
        """

        if self.data is None:
            self.load_data()

        if "clean_text" not in self.data.columns:
            self.process()

        return self.data["clean_text"].tolist()

    def get_articles(self):
        """
        Return the complete processed dataset.
        """

        if self.data is None:
            self.load_data()

        return self.data

    def save_data(self, output_path):
        """
        Save processed articles.
        """

        if self.data is None:
            self.process()

        self.data.to_csv(
            output_path,
            index=False
        )

        return output_path