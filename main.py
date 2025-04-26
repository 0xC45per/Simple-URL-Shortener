#!/usr/bin/env python3

import argparse
import json
import os
import random
import string
import sys

# Constants
DB_FILE = "urls.json"
CODE_LENGTH = 6

def generate_short_code(length=CODE_LENGTH):
    """Generate a random short code"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def load_database():
    """Load URL database from file"""
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {DB_FILE} is corrupted. Creating a new database.")
            return {}
    return {}

def save_database(db):
    """Save URL database to file"""
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

def shorten_url(url):
    """Shorten a URL and store it in the database"""
    db = load_database()
    
    # Check if URL already exists in database
    for code, stored_url in db.items():
        if stored_url == url:
            return code
    
    # Generate a new code
    while True:
        code = generate_short_code()
        if code not in db:
            break
    
    # Add to database
    db[code] = url
    save_database(db)
    
    return code

def get_url(code):
    """Get the original URL for a short code"""
    db = load_database()
    return db.get(code)

def list_urls():
    """List all URLs in the database"""
    db = load_database()
    
    if not db:
        print("No URLs in the database")
        return
    
    print("\nStored URLs:")
    print("-" * 50)
    for code, url in db.items():
        print(f"{code}: {url}")
    print("-" * 50)
    print(f"Total: {len(db)} URLs\n")

def main():
    parser = argparse.ArgumentParser(description="Simple URL shortener")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Shorten command
    shorten_parser = subparsers.add_parser("shorten", help="Shorten a URL")
    shorten_parser.add_argument("url", help="URL to shorten")
    
    # Get command
    get_parser = subparsers.add_parser("get", help="Get original URL from a short code")
    get_parser.add_argument("code", help="Short code to lookup")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all shortened URLs")
    
    args = parser.parse_args()
    
    if args.command == "shorten":
        code = shorten_url(args.url)
        print(f"Short URL: {code}")
        print(f"To get the original URL: python main.py get {code}")
    
    elif args.command == "get":
        url = get_url(args.code)
        if url:
            print(f"Original URL: {url}")
        else:
            print(f"Error: Short code '{args.code}' not found")
    
    elif args.command == "list":
        list_urls()
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
