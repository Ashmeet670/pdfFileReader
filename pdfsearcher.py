import os
from pypdf import PdfReader

search_string = input("Enter the string to search: ")

folder_path = "" #exact file adress of the downloaded certificate folder

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        with open(os.path.join(folder_path, filename), "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                page_text = pdf_reader.pages[page].extract_text()
                if search_string.lower() in page_text.lower():
                    print(f"{filename}, page {page+1}")

                    
