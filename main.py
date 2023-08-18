import chromadb


def main():
    chroma_client = chromadb.PersistentClient(path="./data")
    collection = chroma_client.get_collection("image_collection")
    print("First 5 items from collection:")
    print(collection.peek())
    return

if __name__=="__main__":
    main()