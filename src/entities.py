import pandas as pd
import spacy


class EntityExtractor:

    def __init__(self, model="en_core_web_sm"):
        self.model = model
        self.nlp = None
        self.entities = []

    def load_model(self):
        try:
            self.nlp = spacy.load(self.model)
        except OSError:
            raise RuntimeError(
                "spaCy English model is not installed. "
                "Run: python -m spacy download en_core_web_sm"
            )

    def extract_from_text(self, text):
        if self.nlp is None:
            self.load_model()

        doc = self.nlp(str(text))
        results = []

        for entity in doc.ents:
            results.append({
                "entity": entity.text,
                "type": entity.label_,
                "description": spacy.explain(entity.label_) or "",
                "start": entity.start_char,
                "end": entity.end_char
            })

        return results

    def extract_entities(self, texts):
        all_entities = []

        for article_id, text in enumerate(texts, start=1):
            for item in self.extract_from_text(text):
                item["article_id"] = article_id
                all_entities.append(item)

        self.entities = all_entities

        return pd.DataFrame(
            all_entities,
            columns=[
                "article_id",
                "entity",
                "type",
                "description",
                "start",
                "end"
            ]
        )

    def get_entity_counts(self, entity_df):
        if entity_df.empty:
            return pd.DataFrame(
                columns=["entity", "count"]
            )

        counts = (
            entity_df["entity"]
            .value_counts()
            .reset_index()
        )

        counts.columns = ["entity", "count"]

        return counts

    def save_results(self, entity_df, output_path):
        entity_df.to_csv(
            output_path,
            index=False
        )

        return output_path