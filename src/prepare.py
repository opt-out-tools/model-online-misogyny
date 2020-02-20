import sys
import pandas as pd


def main():
    args = sys.argv[1:]
    input_file = args[1]
    output_file = args[2]
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    df_in = pd.read_csv(input_file)
    print("Input DF info:")
    df_in.info()

    # Balance classes
    # Take the number of elements in the minority class
    min_comm_elements = min(df_in.groupby("label").count().to_numpy())[0]
    df_positive = df_in[df_in["label"] == 1].sample(min_comm_elements, random_state=42)
    df_negative = df_in[df_in["label"] == 0].sample(min_comm_elements, random_state=42)
    df_balanced = pd.concat((df_negative, df_positive)).reset_index(drop=True)
    print("Output DF info:")
    df_balanced.info()

    df_balanced.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()
