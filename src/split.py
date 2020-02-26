import sys
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    """Split dataset into train and test sets"""
    input_files = sys.argv[1:]
    if not input_files:
        raise ValueError("No arguments provided, provide input file as argument.")
    for file in input_files:
        df_in = pd.read_csv(file)
        df_train, df_test = train_test_split(
            df_in,
            train_size=0.8,
            shuffle=True,
            stratify=df_in["label"].to_numpy(),
            random_state=42,
        )
        path = Path(file)
        stem = path.stem
        suffix = path.suffix
        out_name = path.parent.as_posix() + "/" + stem + "-train" + suffix
        print(f"Output: {out_name}")
        df_train.to_csv(out_name, index=False)
        out_name = path.parent.as_posix() + "/" + stem + "-test" + suffix
        print(f"Output: {out_name}")
        df_test.to_csv(out_name, index=False)


if __name__ == "__main__":
    main()
