# Semantic Text2Image Search
This code let's you search your images in a descriptive manner.

![Researcher](frontend/public/researcher.png)

## Usage
### 1. Installation
In a location where you want to place this repo, use the following commands:

    git clone git@github.com:bauerem/semantic-text2image-search.git
    cd semantic-text2image-search
    source setup.sh


### 2. Add Your Own Data

i. Place your images into the backend/images directory.

ii. Make them searchable with the following script:

    source vectorize.sh

### 3. Search
You can now run the software using the command:

    source run_backend.sh

And in another terminal, using the command:

    source run_frontend.sh

## Modifications depending on use-case
- Set the standard embedding function to CLIPProcessor so that Chroma embeds directly
- Tokenization of the query can be sped up by using the CLIPTokenizerFast class in embed.py
- Adjust the 'where_document' parameter in the collection query to only search relvant