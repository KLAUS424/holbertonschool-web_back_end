#!/usr/bin/env python3
"""
Provides statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def get_nginx_stats():
    """Retrieve and display Nginx log statistics from MongoDB"""
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    # Get total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    # Methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    # Count documents for each method
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    # Count status check requests
    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    get_nginx_stats()
