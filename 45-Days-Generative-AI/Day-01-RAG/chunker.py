def create_chunks(cleaned_text):

    chunks = cleaned_text.split("\n\n")

    cleaned_chunks = []

    for chunk in chunks:

        chunk = chunk.strip()

        if chunk:
            cleaned_chunks.append(chunk)

    return cleaned_chunks