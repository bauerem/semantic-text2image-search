import chromadb
from embed import LanguageEmbedder

def test():
    chroma_client = chromadb.PersistentClient(path="./data")
    collection = chroma_client.get_collection("image_collection")
    print("First 5 items from collection:")
    print(collection.peek())

def main():
    chroma_client = chromadb.PersistentClient(path="./data")
    collection = chroma_client.get_collection("image_collection")

    lang_embedder = LanguageEmbedder()
    
    query_string = input("Please enter your search query:")

    query_embedding = lang_embedder([query_string])


    return collection.query(
        query_embeddings=[query_embedding],
        n_results=1,
        ## This needs to be improved:
        #where={"metadata_field": "is_equal_to_this"},
        #where_document={"$contains":"search_string"} 
    )

if __name__=="__main__":
    print(main())