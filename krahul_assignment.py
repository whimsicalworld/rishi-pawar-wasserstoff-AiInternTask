

import json

# Open and read the Dataset.json file
with open('Dataset.json', 'r') as json_file:
    data = json.load(json_file)

# Display the data from the JSON file
print(data)

# Accessing individual PDF links
print("First PDF link:", data['pdf1'])

!pip install pdfplumber
import json
import os
import requests
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import pdfplumber

# Function to download and extract text from a PDF
def process_pdf(pdf_url):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with pdfplumber.open(BytesIO(response.content)) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF from {pdf_url}: {e}")
        return None
    except Exception as e:
        print(f"Error processing PDF from {pdf_url}: {e}")
        return None

# Open and read the Dataset.json file
with open('Dataset.json', 'r') as json_file:
    data = json.load(json_file)

# Create a list of PDF URLs from your JSON data
pdf_urls = []
for key in data:
    if key.startswith('pdf'):
        pdf_urls.append(data.get(key))

# Use a ThreadPoolExecutor for parallel processing
with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers as needed
    results = list(executor.map(process_pdf, pdf_urls))

# Process the extracted text
for i, text in enumerate(results):
    if text:
        print(f"Text from PDF {i+1}:")
        print(text)
        # Do further processing with the extracted text, like saving to a file or analyzing it

!pip install pdfplumber

!pip install pymongo
import json
import requests
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import pdfplumber
from pymongo import MongoClient
import ssl

# MongoDB connection details
client = MongoClient("mongodb+srv://rk:<rk123>@krw.o36y2.mongodb.net/?retryWrites=true&w=majority&appName=krw")  # Replace with your MongoDB URI
db = client["krw"]
collection = db["krc"]





# Create a list of PDF URLs from your JSON data
pdf_urls = []
for key in data:
    if key.startswith('pdf'):
        pdf_urls.append(data.get(key))


# Connect to MongoDB

# Process the extracted text, and store it in MongoDB
for i, text in enumerate(results):
    if text:
        document = {
            "pdf_url": pdf_urls[i],
            "text": text
        }
        # Store document in MongoDB
        collection.insert_one(document)
        print(f"Text from PDF {i+1} saved to MongoDB.")
    else:
        print(f"Failed to extract text from PDF {i+1}.")






