from embed import ImageEmbedder
from pathlib import Path
import chromadb

# https://docs.trychroma.com/getting-started

chroma_client = chromadb.PersistentClient(path="./data") #(host='localhost', port=50051)

# Get image paths
image_folder = "./images"
image_files = list(Path(image_folder).glob("*.jpeg"))  # adapt this if you have different image formats

# Embedder
embedder = ImageEmbedder()

collection = chroma_client.get_or_create_collection(name="image_collection") # (dimension=512, metric='Cosine')

# Add vectors to the collection
for i, image_file in enumerate(image_files):
    
    embedding = embedder([
        image_file
    ])


    collection.upsert(
        embeddings=embedding,
        metadatas=[{"uri": str(image_file)}],
        documents=[str(image_file)],
        ids=[f"{i}"],
    )

print(collection.count())
