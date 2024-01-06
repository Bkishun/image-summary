import pytesseract as pyt
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2

def image_to_text(filename):
    img = cv2.imread(filename)
    text = pyt.image_to_string(img)
    return text
