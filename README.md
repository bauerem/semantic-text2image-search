# Semantic Text2Image Search
This repo implements a simple terminal-based semantic image search.

## Usage
### Setup
    git clone git@github.com:bauerem/semantic-text2image-search.git
    cd semantic-text2image-search
    python3 -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt

### Initialize DB
Make your data folders. They are excluded from this repo/

    mkdir data
    mkdir images

Place all your images into the images folder and add their embeddings to the database:

    python vectorize.py

## Use
Now you can search your images by using the following command:

    python main.py

## Modifications depending on use-case
- Set the standard embedding function to CLIPProcessor so that Chroma embeds directly
- Tokenization of the query can be sped up by using the CLIPTokenizerFast class in embed.py
- Adjust the 'where_document' parameter in the collection query to only search relvant