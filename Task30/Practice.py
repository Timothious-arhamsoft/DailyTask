from typing import List
import re
from sentence_transformers import SentenceTransformer

# Fixed-Size Chunking 
# Split the text into units (words, in this case)
def word_splitter(source_text: str) -> List[str]:
    source_text = re.sub(r"\s+", " ", source_text) # Replace multiple whitespces
    return re.split(r"\s", source_text) # Split by single whitespace

def get_chunks_fixed_size_with_overlap(text: str, chunk_size: int, overlap_fraction: float = 0.2) -> List[str]:
    text_words = word_splitter(text)
    overlap_int = int(chunk_size * overlap_fraction)
    chunks = []
    for i in range(0, len(text_words), chunk_size):
        chunk_words = text_words[max(i - overlap_int, 0): i + chunk_size]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
    return chunks

# Recursive Chunking

def recursive_chunking(text: str, max_chunk_size: int = 1000) -> List[str]:
    # Base case: if text is small enough, return as single chunk
    if len(text) <= max_chunk_size:
        return [text.strip()] if text.strip() else []

    # Try separators in priority order
    separators = ["\n\n", "\n", ". ", " "]

    for separator in separators:
        if separator in text:
            parts = text.split(separator)
            chunks = []
            current_chunk = ""

            for part in parts:
                # Check if adding this part would exceed the limit
                test_chunk = current_chunk + separator + part if current_chunk else part

                if len(test_chunk) <= max_chunk_size:
                    current_chunk = test_chunk
                else:
                    # Save current chunk and start new one
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = part

            # Add the final chunk
            if current_chunk:
                chunks.append(current_chunk.strip())

            # Recursively process any chunks that are still too large
            final_chunks = []
            for chunk in chunks:
                if len(chunk) > max_chunk_size:
                    final_chunks.extend(recursive_chunking(chunk, max_chunk_size))
                else:
                    final_chunks.append(chunk)

            return [chunk for chunk in final_chunks if chunk]

    # Fallback: split by character limit if no separators work
    return [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

# Document-Based Chunking

def markdown_document_chunking(text: str) -> List[str]:
    # Split by markdown headers (# ## ### etc.)
    header_pattern = r'^#{1,6}\s+.+$'
    lines = text.split('\n')

    chunks = []
    current_chunk = []

    for line in lines:
        # Check if this line is a header
        if re.match(header_pattern, line, re.MULTILINE):
            # Save previous chunk if it has content
            if current_chunk:
                chunk_text = '\n'.join(current_chunk).strip()
                if chunk_text:
                    chunks.append(chunk_text)

            # Start new chunk with this header
            current_chunk = [line]
        else:
            # Add line to current chunk
            current_chunk.append(line)

    # Add final chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk).strip()
        if chunk_text:
            chunks.append(chunk_text)

    return chunks

# Implementation of Word Embedding
def word_embedding(text: str) -> List[float]:
    corpus = text

    print("Corpus: ")
    print(corpus)
    # Load Sentence-BERT model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Encode sentences into embeddings
    embeddings = model.encode(corpus)

    print("Embeddings: ")
    print(embeddings)


def main():
    print("Fixed-Size Chunking with Overlap Example")
    text = "This is a sample text that will be split into chunks of fixed size with overlap."
    chunk_size = 5
    overlap_fraction = 0.2
    chunks = get_chunks_fixed_size_with_overlap(text, chunk_size, overlap_fraction)
    # for i, chunk in enumerate(chunks):
    #     print(f"Chunk {i + 1}: {chunk}")

    print("\nRecursive Chunking Example")
    max_chunk_size = 20
    recursive_chunks = recursive_chunking(text, max_chunk_size)
    # for i, chunk in enumerate(recursive_chunks):
    #     print(f"Chunk {i + 1}: {chunk}")  

    print("\nMarkdown Document Chunking Example")
    markdown_text = """
    # Header 1
    This is the content under Header 1.

    ## Header 2
    This is the content under Header 2.

    ### Header 3
    This is the content under Header 3.
    """
    markdown_chunks = markdown_document_chunking(markdown_text)
    # for i, chunk in enumerate(markdown_chunks):
    #     print(f"Chunk {i + 1}: {chunk}")

    print("\nWord Embedding Example")
    text = ["Machine learning models require large datasets.","Artificial intelligence is changing the world.",
    "Neural networks are inspired by the human brain.","Deep learning is a subset of machine learning.",
    "Data preprocessing is essential for better accuracy."]
    word_embedding(text)
if __name__ == "__main__":
    main()