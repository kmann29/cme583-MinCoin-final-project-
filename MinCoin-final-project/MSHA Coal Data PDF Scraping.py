import pytesseract
import os
from pdf2image import convert_from_path
import re
import pandas as pd

# Set the Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\aarna\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#folder containing  PDFs
pdf_folder = 'pdfs'

# List of accident classification keywords
keywords = [
    "CO Poisoning", "Confined Space", "Drowning", "Electrical", "Engulfment",
    "Entrapment", "Exploding Vessels Under Pressure", "Explosives and Breaking Agents",
    "Fall of Face, Rib, Side or Highwall", "Fall of Roof Or Back",
    "Falling, Rolling, or Sliding of Rock Or Material Of Any Kind", "Fire", "Hand Tools",
    "Handling Material", "Hoisting", "Ignition Or Explosion Of Gas Or Dust",
    "Impoundment", "Inundation", "Machinery", "Non-Powered Haulage", "Other",
    "Powered Haulage", "Slip or Fall Of Person", "Stepping Or Kneeling On Object",
    "Striking or Bumping"
]

# State abbreviations
state_abbreviations = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA'
    , 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
    'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

#Data lists
accident_keywords_list = []
state_classifications_list = []
dates_list = []

# Iterate through all PDF files in the folder
for pdf_filename in os.listdir(pdf_folder):
    if pdf_filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, pdf_filename)

        # Convert each page of the PDF to an image
        images = convert_from_path(pdf_path)

        # Extract text from each image (PDF page)
        text = ""
        for i, image in enumerate(images):
            page_text = pytesseract.image_to_string(image)
            text += f"--- Page {i + 1} ---\n{page_text}\n"

        # Print the PDF file being processed (for tracking)
        print(f"\nProcessing {pdf_filename}...\n")

        # Extract accident classification keywords
        matches_keywords = [keyword for keyword in keywords if keyword in text]
        accident_keywords_list.extend(matches_keywords)

        # Extract state abbreviations
        matches_states = re.findall(r'\b(' + '|'.join(state_abbreviations) + r')\b', text)
        state_classifications_list.extend(matches_states)

        # Extract dates in MM/DD/YYYY format
        matches_dates = re.findall(r'\b(0[1-9]|1[0-2])/[0-3][0-9]/\d{4}\b', text)
        dates_list.extend(matches_dates)


        # Extract Date/Time after the "3. Date/Time of Accident" label
        date_time_match = re.search(
            r'3\.\s*Date/Time of Accident.*?(\d{2}/\d{2}/\d{4}\s+\d{1,2}:\d{2}\s*(AM|PM))', text, re.S
        )
        if date_time_match:
            # Extract the full date and time
            date_time_of_accident = date_time_match.group(1).strip()
            dates_list.append(date_time_of_accident)
        else:
            dates_list.append("Not found")  # If no date is found, append a placeholder



# Create DataFrames
accident_keywords_df = pd.DataFrame({'Accident Classification': accident_keywords_list})
state_classifications_df = pd.DataFrame({'State Abbreviation': state_classifications_list})
date_df = pd.DataFrame({'Date and Time of Accident': dates_list})

# Save DataFrames to CSV files
accident_keywords_df.to_csv("accident_keywords.csv", index=False)
state_classifications_df.to_csv("state_classifications.csv", index=False)
date_df.to_csv("dates.csv", index=False)

print("\nDataFrames created and saved as CSV files!")
