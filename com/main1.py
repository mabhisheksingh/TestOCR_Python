import pytesseract
from pdf2image import convert_from_path

from com.utils.TimerUtils import TimerUtils


def extract_text_from_pdf_to_image(pdf_path):
    print(pdf_path)
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, first_page=2, last_page=5)

    # Extract text from each image using OCR
    extracted_text = ""
    for image in images:
        print("IMAGE ", image)
        # Perform OCR on the image
        text = pytesseract.image_to_string(image, lang='Devanagari')

        # Append the extracted text to the result
        extracted_text += text

    return extracted_text


# Path to the PDF file
pdf_path = '/home/abhishek/Desktop/Python/TestOCRPy1/resources/313.pdf'
pdf_text = ''
with TimerUtils():
    # Extract text from the PDF and convert it to an image
    pdf_text = extract_text_from_pdf_to_image(pdf_path)
# Print the extracted text
print(pdf_text)
