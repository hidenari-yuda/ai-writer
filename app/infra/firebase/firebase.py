import datetime
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from firebase_admin import storage
from google.cloud import storage

global GOOGLE_APPLICATION_CREDENTIALS
global FIREBASE_STORAGE_BUCKET


class Firebase:
    db = None
    bucket = None

    def __init__(self):
        pass

    def new_firestore(self):
        GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

        cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        Firebase.db = db

    # データベースから取得
    def get_firestore(self, collection_name) -> dict:
        db = firestore.client()
        users = db.collection(collection_name)
        docs = users.stream()

        for doc in docs:
            print(doc.to_dict())

        return doc.to_dict()

    # データベースから取得
    def get_firestore_where(self, collection_name) -> list(dict):
        db = firestore.client()
        users = db.collection(collection_name).where('active', '==', True).where(
            'created_at', '>', datetime.datetime.now())
        docs = users.stream()
        list = []

        for doc in docs:
            print(doc.to_dict())
            list.append(doc.to_dict())

        return list

    # データベースに追加
    def set_firestore(self, collection_name, data) -> dict:
        db = firestore.client()
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(data)

        return doc_ref

    def new_storage(self):
        GOOGLE_APPLICATION_CREDENTIALS = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        FIREBASE_STORAGE_BUCKET = os.environ["FIREBASE_STORAGE_BUCKET"]

        cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
        firebase_admin.initialize_app(
            cred, {'storageBucket': FIREBASE_STORAGE_BUCKET})
        bucket = storage.bucket()

        Firebase.bucket = bucket

    def upload_blob(self, source_file_name, destination_blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(
            "File {} uploaded to {}.".format(
                source_file_name, destination_blob_name
            )
        )

    def download_blob(self, source_blob_name, destination_file_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print(
            "Blob {} downloaded to {}.".format(
                source_blob_name, destination_file_name
            )
        )

    def blob_list(self, prefix=""):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blobs = list(bucket.list_blobs(prefix=prefix))
        print(
            "Blob list to {}.".format(
                blobs
            )
        )
        return blobs

    def blob_delete(self, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(blob_name)
        blob.delete()
        print(
            "Blob {} deleted.".format(
                blob_name
            )
        )

    def blob_exists(self, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(blob_name)
        return blob.exists()

    def blob_public_url(self, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(blob_name)
        return blob.public_url

    def blob_make_public(self, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(blob_name)
        blob.make_public()
        return blob.public_url

    def blob_make_private(self, blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(FIREBASE_STORAGE_BUCKET)
        blob = bucket.blob(blob_name)
        blob.make_private()
        return blob.public_url
