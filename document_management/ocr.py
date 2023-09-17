import pytesseract
from PIL import Image

def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    image_path = "path/to/image.png"
    ocr_text = perform_ocr(image_path)
    print(ocr_text)
