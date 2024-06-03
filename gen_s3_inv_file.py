import csv
import boto3
import awswrangler as wr

# Initialize your AWS session
session = boto3.Session()

# Define your bucket and prefixes
bucket = "your-bucket-name"
prefixes = ["prefix1/", "prefix2/"]

# Define the CSV file path
csv_file_path = "output.csv"

# Write the header if the file doesn't exist
with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["bucket", "key"])
    if file.tell() == 0:
        writer.writeheader()

# Iterate over prefixes and write to CSV
for prefix in prefixes:
    s3_uri = f"s3://{bucket}/{prefix.strip()}"
    print(f"Listing objects at {s3_uri}")
    pages = wr.s3.list_objects(
        s3_uri,
        boto3_session=session,
        chunked=True,
    )

    for page in pages:
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["bucket", "key"])
            for item in page:
                writer.writerow({"bucket": bucket, "key": item.split("/", 3)[-1]})
