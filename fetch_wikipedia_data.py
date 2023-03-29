#pip install wikipedia-api
#pip install spacy
#python -m spacy download en_core_web_sm
#pip install pandas
#pip install textblob

import wikipediaapi
import spacy
import pandas as pd
from textblob import TextBlob

def fetch_wikipedia_page_content(page_name, wiki_lang):
    page = wiki_lang.page(page_name)
    return page.text if page.exists() else None

def preprocess_text(text, nlp):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

def label_func(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"

    return label

def extract_and_label_information(sentences, label_func):
    data = []
    for sentence in sentences:
        label = label_func(sentence)
        if label:
            data.append({"text": sentence, "label": label})
    return data

def main():
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Load Wikipedia pages list
    with open("wikipedia_pages.txt", "r") as f:
        page_names = [line.strip() for line in f.readlines()]

    # Initialize Wikipedia API
    wiki_lang = wikipediaapi.Wikipedia("en")

    # Process Wikipedia pages and build dataset
    dataset = []
    for page_name in page_names:
        print(f"Processing page: {page_name}")
        content = fetch_wikipedia_page_content(page_name, wiki_lang)
        if content:
            sentences = preprocess_text(content, nlp)
            data = extract_and_label_information(sentences, label_func)
            dataset.extend(data)

    # Save dataset as CSV
    df = pd.DataFrame(dataset)
    df.to_csv("training_data.csv", index=False)

if __name__ == "__main__":
    main()
