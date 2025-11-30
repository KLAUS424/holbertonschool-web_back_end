#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
Database: logs, Collection: nginx.
"""
from pymongo import MongoClient

def log_stats():
    """
    Provides statistics about Nginx logs stored in the MongoDB 'logs' database
    and 'nginx' collection.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Access the database and collection
    db = client.logs
    nginx_collection = db.nginx

    # 1. Total number of documents (logs)
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    # 2. Method counts
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        # Use tabulation (\t) as requested
        print(f"\tmethod {method}: {count}")

    # 3. Documents with method=GET and path=/status
    status_count = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_count} status check")

if __name__ == "__main__":
    log_stats()
