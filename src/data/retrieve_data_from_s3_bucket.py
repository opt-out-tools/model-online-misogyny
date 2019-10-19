import boto3
from botocore.exceptions import ClientError


def download_dataset(file_path: str):
    """Downloads the stanford dataset."""
    client = boto3.client("s3", aws_access_key_id="", aws_secret_access_key="")

    try:
        client.download_file("opt-out-tools-data", "stanford.csv", file_path)

    except ClientError:
        print("Dataset does not exist")


if __name__ == "__main__":
    download_dataset("../../data/processed/stanford.csv")
