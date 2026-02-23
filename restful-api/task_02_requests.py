#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and save to CSV"""
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their IDs and titles"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # print the status code of the response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print(f"Failed to fetch posts.")

def fetch_and_save_posts(filename):
    """Fetch posts from JSONPlaceholder and save them to a CSV file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        with open(filename, mode='w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for post in posts:
                writer.writerow({'id': post['id'], 
                                 'title': post['title'], 
                                 'body': post['body']
                                 })
            print(f"Posts saved to {filename}")
    
    # calls required functions
    if __name__ == "__main__":
        fetch_and_print_posts(filename)
        fetch_and_save_posts("posts.csv")