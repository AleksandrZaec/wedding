from django.conf import settings
import boto3


def delete_from_storage(file_name):
    """
    Удаляет файл из облачного хранилища по заданному имени.
    """
    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=settings.AWS_S3_ENDPOINT_URL
    )

    try:
        s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_name)
        print(f"Successfully deleted file: {file_name}")
    except Exception as e:
        print(f"Error deleting file: {e}")
