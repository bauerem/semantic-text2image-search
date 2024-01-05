import chromadb
from embed import LanguageEmbedder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

chroma_client = chromadb.PersistentClient(path="./data")
collection = chroma_client.get_collection("image_collection")
lang_embedder = LanguageEmbedder()

app = FastAPI()

origins = ["http://localhost", "http://localhost:8080", "http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/images", StaticFiles(directory="images/"), name="images")


@app.get("/")
async def root(query: str | None = None):
    if query:
        query_embedding = lang_embedder([query])

        return {
            "result": collection.query(
                query_embeddings=[query_embedding],
                n_results=1,
                ## This needs to be improved:
                # where={"metadata_field": "is_equal_to_this"},
                # where_document={"$contains":"search_string"}
            )
        }
    else:
        return {}


def test():
    chroma_client = chromadb.PersistentClient(path="./data")
    collection = chroma_client.get_collection("image_collection")
    print("First 5 items from collection:")
    print(collection.peek())