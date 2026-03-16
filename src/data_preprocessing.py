import re
import nltk

nltk.download("punkt")

def clean_text(text):

    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)

    return text


def preprocess_dataset(dataset):

    processed = []

    for item in dataset:

        article = clean_text(item["article"])
        summary = clean_text(item["highlights"])

        processed.append({
            "article": article,
            "summary": summary
        })

    return processed