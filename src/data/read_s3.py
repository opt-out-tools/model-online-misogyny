import boto3
from boto3_type_annotations.s3 import Client
from botocore.exceptions import ClientError


def download_dataset(s3_client: Client):
    """Downloads the stanford dataset."""
    try:
        s3_client.download_file(
            "opt-out-tools-data", "stanford.csv", "../../data/raw/stanford.csv"
        )

    except ClientError:
        print("Dataset does not exist")


if __name__ == "__main__":
    download_dataset(boto3.client("s3"))
