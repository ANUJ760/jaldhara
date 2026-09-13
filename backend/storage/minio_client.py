from minio import Minio
from ..config import settings

client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=settings.MINIO_SECURE
)

def init_buckets():
    buckets = ["dem-data", "imagery", "sim-output", "exports"]
    for bucket in buckets:
        if not client.bucket_exists(bucket):
            client.make_bucket(bucket)

def upload_file(bucket: str, object_name: str, file_path: str):
    client.fput_object(bucket, object_name, file_path)
    return f"{settings.MINIO_ENDPOINT}/{bucket}/{object_name}"

def get_presigned_url(bucket: str, object_name: str):
    return client.presigned_get_object(bucket, object_name)
