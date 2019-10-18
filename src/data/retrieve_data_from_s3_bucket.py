from botocore.exceptions import ClientError


def download_dataset(s3_client, file_path: str):
    """Downloads the stanford dataset."""
    try:
        s3_client.download_file("opt-out-tools-data", "stanford.csv", file_path)

    except ClientError:
        print("Dataset does not exist")
