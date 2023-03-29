# nlmate - Data preprocessing for NLMs
An open-source solution for scraping, preprocessing, and labeling datasets from specified Wikipedia pages for using in training Natural Language Processing (NLP) models.


![Pipeline Test](https://github.com/LibreCS/nlmate/actions/workflows/test_pipeline.yml/badge.svg) ![GitHub last commit](https://img.shields.io/github/last-commit/LibreCS/nlmate) ![GitHub](https://img.shields.io/github/license/LibreCS/nlmate)

## Prerequisites

- Python 3.6 or higher
- Wikipedia API package
- spaCy package
- TextBlob package
- pandas package

Install the required packages using the following command:
```
pip install wikipedia-api spacy textblob pandas
```

## Usage

1. (Optional) Generate a list of random Wikipedia page names using `generate_random_wikipedia_pages.py`. By default, it generates 50 random page names:

    This will create a file named `wikipedia_pages.txt` containing the Wikipedia page names.

    To use specified Wikipedia pages, enter the page titles line by line in the file `wikipedia_pages.txt` rather than using the random page generation script.


2. Run `fetch_and_label_wikipedia_data.py` to fetch content from the listed Wikipedia pages, preprocess the data, label it, and save the resulting dataset as a CSV file:

```
python fetch_and_label_wikipedia_data.py
```


The output file `training_data.csv` will contain the structured training dataset.

## Customization

To customize the labeling function, edit the `label_func` function in `fetch_and_label_wikipedia_data.py`. This function should take a text input and return a label based on the content of the text. The current implementation uses TextBlob sentiment analysis to assign "positive", "negative", or "neutral" labels based on the sentiment polarity of the text.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




