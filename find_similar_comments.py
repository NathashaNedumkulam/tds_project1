from sentence_transformers import SentenceTransformer
import numpy as np

# File paths
input_file = "C:/Users/natha/tds_project1/data/comments.txt"
output_file = "C:/Users/natha/tds_project1/data/comments-similar.txt"

# Load comments
with open(input_file, "r", encoding="utf-8") as f:
    comments = [line.strip() for line in f.readlines()]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Compute embeddings
embeddings = model.encode(comments, convert_to_tensor=True)

# Compute cosine similarity matrix
similarities = np.inner(np.asarray(embeddings), np.asarray(embeddings))


# Find most similar pair (excluding self-similarity)
np.fill_diagonal(similarities, 0)  # Ignore diagonal (self-matching)
i, j = np.unravel_index(np.argmax(similarities), similarities.shape)

# Save most similar comments
with open(output_file, "w", encoding="utf-8") as f:
    f.write(comments[i] + "\n")
    f.write(comments[j] + "\n")

print(f"✅ Most similar comments saved to {output_file}")

