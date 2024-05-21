import os
import pytesseract
from PIL import Image
from com.utils.TimerUtils import TimerUtils

os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/5/tessdata/'
print("processing start...")


# def ocr_image(image_path, lang='eng'):
def ocr_image(image_path, lang='Devanagari'):
    """Perform OCR on an image file."""
    try:
        # Open image
        img = Image.open(image_path)
        # Perform OCR
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None


# Example usage
image_path = '/home/abhishek/Desktop/Python/TestOCRPy1/resources/image.png'
with TimerUtils():
    recognized_text = ocr_image(image_path)

print("****Printing start***")
print(recognized_text)
print("****Printing End***")
