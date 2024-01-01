from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from pytesseract import pytesseract
from fpdf import FPDF
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
            return str(e)

class MyApp(App):
    def build(self):
        self.ocr = OCR()
        self.layout = BoxLayout(orientation='vertical')
        self.filechooser = FileChooserIconView()
        self.filechooser.bind(on_submit=self.load_image)
        self.layout.add_widget(self.filechooser)
        self.label = Label(size_hint_y=None, height=750)
        self.layout.add_widget(self.label)
        return self.layout

    def load_image(self, instance, value, touch):
        if value:
            text = self.ocr.extract(value[0])
            self.label.text = text
            self.write_to_pdf(text)

    def write_to_pdf(self, text):
        text = text.replace('\u2014', '--')  # replace em dash with double hyphen
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        pdf.multi_cell(0, 10, txt = text)
        pdf.output("output.pdf")


if __name__ == '__main__':
    MyApp().run()