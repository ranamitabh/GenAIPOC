from pytesseract import pytesseract
import os

class OCR:
    def __init__(self):
        self.path = "/usr/local/bin/tesseract"


    def extract(self, image):
        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            print(e)


ocr=OCR()
# text=ocr.extract("image.png")
text=ocr.extract("Images/test1.png")
print(text)