
import cv2
import pytesseract
import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Configure Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Adjust this path if needed


def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def extract_text(image):
    return pytesseract.image_to_string(image)


def detect_document_type(text):
    if "GOVT. OF INDIA" in text or "AADHAAR" in text:
        return "Aadhaar"
    elif "INCOME TAX DEPARTMENT" in text or "Permanent Account Number" in text:
        return "PAN"
    else:
        return "Unknown"


def extract_information(text, doc_type):
    info = {}
    if doc_type == "Aadhaar":
        # name_search = re.search(r'\b[A-Z]+\b.*\b[A-Z]+\b', text)
        # info['Name'] = name_search.group(0) if name_search else "Not Found"
        aadhaar_number_search = re.search(r'\b\d{4} \d{4} \d{4}\b', text)
        info['Aadhaar Number'] = aadhaar_number_search.group(0) if aadhaar_number_search else "Not Found"
    elif doc_type == "PAN":
        # name_search = re.search(r'[A-Z\s]+', text)
        # info['Name'] = name_search.group(0).strip() if name_search else "Not Found"
        pan_number_search = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]{1}', text)
        info['PAN Number'] = pan_number_search.group(0) if pan_number_search else "Not Found"
    return info


def main():
    Tk().withdraw()
    image_path = askopenfilename(title="Select Aadhaar or PAN card image")
    if not image_path:
        print("No file selected.")
        return

    preprocessed_image = preprocess_image(image_path)
    text = extract_text(preprocessed_image)

    doc_type = detect_document_type(text)
    if doc_type == "Unknown":
        print("Document type could not be identified.")
        return

    extracted_info = extract_information(text, doc_type)

    print(f"Document Type: {doc_type}")
    for key, value in extracted_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()




