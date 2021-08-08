from google.cloud import storage
import os


class UploadToStorage:

    def __init__(self):
        self.KEY_PATH = "./secret/key-file.json"
        self.storage_client = storage.Client.from_service_account_json(self.KEY_PATH)
        self.FILE_PATH = "./res"

    def create_bucket(self, bucket_name):
        try:
            bucket = self.storage_client.create_bucket(bucket_name)
            return bucket
        except Exception as err:
            print(err.args)
            raise Exception("Bucket Creation Failed")

    def list_buckets(self):
        try:
            buckets = list(self.storage_client.list_buckets())
            print(buckets)
        except Exception as err:
            raise Exception('Buckets fetching failed')

    def upload_file(self, bucket, source_file_name, destination_file_name):
        try:
            blob = bucket.blob(destination_file_name)
            blob.upload_from_filename(os.path.join(self.FILE_PATH, source_file_name))
        except Exception as err:
            print(err.args)
            raise Exception('File Upload Failed')

    def solve(self):
        try:
            self.list_buckets()
            bucket = self.create_bucket("assignment-customers-orders")
            # bucket = self.storage_client.bucket("assignment-customers-orders")
            self.upload_file(bucket, "Customers.csv", "customers.csv")
            self.upload_file(bucket, "Orders.csv", "orders.csv")
            print(bucket)
        except Exception as err:
            print(err.args[0])




