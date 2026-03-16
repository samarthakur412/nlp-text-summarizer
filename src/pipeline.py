from src.model import TextSummarizer

summarizer = TextSummarizer()

def summarize_text(text):

    summary = summarizer.summarize(text)

    return summary