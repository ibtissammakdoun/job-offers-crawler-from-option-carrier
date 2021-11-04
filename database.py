import pymongo
from pymongo import MongoClient
def insert_documents(docs):
    client = MongoClient(host="localhost", port=27017)
    db = client.jobsDb
    maroc_jobs = db.JobsMaroc
    result = maroc_jobs.insert_many(docs)
    print(f"Multiple tutorials: {result.inserted_ids}")
    client.close()


def insert_documents2(docs):
    client = MongoClient(host="localhost", port=27017)
    db = client.jobsDb
    maroc_jobs = db.JobsFrance
    result = maroc_jobs.insert_many(docs)
    print(f"Multiple tutorials: {result.inserted_ids}")
    client.close()