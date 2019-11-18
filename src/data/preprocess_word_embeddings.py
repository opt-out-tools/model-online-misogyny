from os.path import exists
import numpy as np


def get_embeddings(embedding_path):
    embeddings_index = {}
    file_name = embedding_path

    with open(file_name, encoding="utf-8") as file:
        for line in file:
            values = line.split(" ")
            word = values[0]
            embedding = np.asarray(values[1:], dtype="float32")
            embeddings_index[word] = embedding

    print("Word embeddings: %d" % len(embeddings_index))
    return embeddings_index


# Prepare word embedding matrix
def get_embedding_matrix(embeddings_index, word_index, max_nb_words, dimension):
    nb_words = min(max_nb_words, len(word_index))
    word_embedding_matrix = np.zeros((nb_words + 1, dimension))
    for word, i in word_index.items():
        if i > max_nb_words:
            continue
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            word_embedding_matrix[i] = embedding_vector

    print(
        "Null word embeddings: %d" % np.sum(np.sum(word_embedding_matrix, axis=1) == 0)
    )
    return word_embedding_matrix


# Initialize embedding matrix. If it exists, load it, otherwise create it
def init_embeddings(
    word_index, max_number_of_words, embedding_dimension, word_embedding_path
):
    cache_filename = "embedding_matrix.npy"

    if exists(cache_filename):
        word_embedding_matrix = np.load(cache_filename)
    else:
        # Prepare embedding matrix to be used in Embedding Layer
        embeddings_index = get_embeddings(word_embedding_path)
        word_embedding_matrix = get_embedding_matrix(
            embeddings_index, word_index, max_number_of_words, embedding_dimension
        )
        np.save(cache_filename, word_embedding_matrix)
    return word_embedding_matrix
