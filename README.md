# URL Shortener Project

A simple URL shortener built using FastAPI and Python.

## Features

* Shorten URLs using a unique identifier
* Retrieve original URLs by their shortened identifier

## Requirements

* Python 3.12+
* FastAPI
* Pydantic
* uvicorn

## Installation

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```
## Running the Application

To start the application, run:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
## API Endpoints

### Shorten URL

* **POST** `/`: Shorten a URL
	+ Request Body: `{"url": "https://example.com"}`
	+ Response: `{"short_url": "https://example.com/abc123"}`
### Get Original URL

* **GET** `/{short_url_id}`: Get the original URL by its shortened identifier
	+ Response: `{"original_url": "https://example.com"}`

### Author [RTMoo]