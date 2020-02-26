import sys
import pandas as pd


def main():
    """Here one wold implement preliminary operations e.g. removing NAs"""
    args = sys.argv[1:]
    input_file = args[0]
    output_file = args[1]
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    df_in = pd.read_csv(input_file)
    print("Input DF info:")
    df_in.info()

    df_balanced = df_in
    print("Output DF info:")
    df_balanced.info()

    df_balanced.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()
