# rishi-pawar-wasserstoff-AiInternTask

AiInternTask
This repository contains a Python program designed to download, extract, and process text from a set of PDFs provided in a JSON dataset. The PDFs are processed in parallel for efficiency, and the extracted text can be further analyzed or saved. MongoDB is used to store or manage the data.

Table of Contents
System Requirements
Setup Instructions
Usage
Explanation of the Solution
System Requirements
Python 3.x
Required Python packages:
requests
pdfplumber
pymongo
Ensure you have pip installed to manage Python packages.

Setup Instructions
Clone the Repository:


git clone https://github.com/rishi-pawar/wasserstoff/AiInternTask.git
cd AiInternTask
Install the Required Packages: Install the necessary Python dependencies:


pip install -r requirements.txt
Alternatively, you can manually install the packages:


pip install requests pdfplumber pymongo
Prepare the Dataset: Ensure you have a Dataset.json file in the project directory, structured like this:

json
Copy code
{
  "pdf1": "http://example.com/sample1.pdf",
  "pdf2": "http://example.com/sample2.pdf",
  ...
}
Run the Script: Execute the Python script to download and process PDFs:


python krahul_assignment.py
Usage
This script reads a JSON file (Dataset.json) containing PDF URLs, downloads the PDFs, and extracts their text content. The text is then printed or can be further processed (e.g., saved or analyzed). MongoDB functionality is included to store data but requires configuration.

Example JSON Structure:
json
Copy code
{
  "pdf1": "http://example.com/sample1.pdf",
  "pdf2": "http://example.com/sample2.pdf"
}
Explanation of the Solution
Reading the Dataset: The script starts by loading a Dataset.json file, which contains URLs to PDFs. These PDFs are processed for further text extraction.

Downloading and Extracting Text: Using the pdfplumber library, the script downloads each PDF and extracts its text. This is done efficiently with the help of ThreadPoolExecutor, which allows for parallel processing.

MongoDB Integration: MongoDB is set up to store extracted information, though additional steps would be required to fully configure the database and handle data storage.

Error Handling: The script includes error handling for failed PDF downloads and processing, logging appropriate messages for each error.
