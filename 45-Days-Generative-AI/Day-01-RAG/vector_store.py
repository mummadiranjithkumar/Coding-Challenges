import chromadb


client = chromadb.Client()

collection = client.get_or_create_collection(
    name="resume_chunks"
)


def store_embeddings(chunks, embeddings):

    ids = []

    for index in range(len(chunks)):
        ids.append(str(index))

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

    return collection