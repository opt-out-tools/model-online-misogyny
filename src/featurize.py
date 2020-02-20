import sys
import joblib
import numpy as np
import pandas as pd
import spacy


def main():
    """Take text from input dataframe and vectorize it to build a feature matrix"""
    try:
        input_file, output_file = sys.argv[1], sys.argv[3]
    except (IndexError, ValueError) as error:
        print(error)
        print("Error: please specify input and output files.")
        sys.exit()
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    df_in = pd.read_csv(input_file)
    print("Loading language model...")
    nlp = spacy.load("en_core_web_md")
    # The .pipe() method batch processes all the text (will take a little while)
    print("Creating embeddings...")
    docs = list(nlp.pipe(df_in["text"]))
    feature_matrix = np.array(list(map(lambda x: x.vector, docs)))
    print(f"The feature matrix has dimensions {feature_matrix.shape}.")
    with open(output_file, "wb") as handler:
        joblib.dump(feature_matrix, handler, compress="zlib")


if __name__ == "__main__":
    main()
