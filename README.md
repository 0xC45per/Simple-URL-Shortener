# 🔗 Simple URL Shortener

A lightweight command-line tool to create and manage shortened URLs.

## ✨ Features

- 🔹 Shorten long URLs to easy-to-remember codes
- 🔍 Retrieve original URLs using their short codes
- 📋 List all your shortened URLs
- 💾 Store URLs locally in a JSON database

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/0xC45per/simple-url-shortener.git
cd simple-url-shortener
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py <command> [options]
```

## ⚙️ Commands

- `shorten`: Shorten a URL
- `get`: Get original URL from a short code
- `list`: List all shortened URLs

## 📝 Examples

### Shorten a URL:
```bash
python main.py shorten https://www.example.com/very/long/path/to/resource
```

### Get the original URL:
```bash
python main.py get Abc123
```

### List all stored URLs:
```bash
python main.py list
```

## 📌 Notes

- This is a simple local URL shortener - to make it work as a web service, you would need to integrate it with a web framework
- The shortened codes are stored in a local file (`urls.json`)
- Each short code is 6 characters by default, using letters and numbers

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.