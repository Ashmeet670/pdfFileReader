import os
from pypdf import PdfReader

search_text = input("Enter the text to search: ")

folder_path = "" #the exact path of the folder containing all the pdf files

fileFound = False

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        with open(os.path.join(folder_path, filename), "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page in range(len(pdf_reader.pages)):
                page_text = pdf_reader.pages[page].extract_text()
                if search_text.lower() in page_text.lower():
                    print(f"{filename}, page {page+1}")
                    fileFound = True
                
if(fileFound == False):
   print("no such file with the provided text")
