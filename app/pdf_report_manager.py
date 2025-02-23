# from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import textwrap
import os

class PDFManager:
    def __init__(self, filename):
        self.filename = filename
        doc = SimpleDocTemplate("formatted.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        self.downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #save as per your system or prefered directory
        self.file_path = os.path.join(self.downloads_folder, self.filename)
        self.text_list = []

    def add_text(self, new_text):
        self.text_list.append(new_text)
        self.generate_pdf()

    def generate_pdf(self):
        pdf = canvas.Canvas(self.file_path, pagesize=letter)
        width, height = letter  
        pdf.setFont("Helvetica", 12)
        y_position = height - 40
        line_height = 15 
        margin = 40

        for text in self.text_list:
            wrapped_lines = textwrap.wrap(text, width=100)
            for line in wrapped_lines:
                if y_position < 40:
                    pdf.showPage()
                    pdf.setFont("Helvetica", 12)
                    y_position = height - 40
                pdf.drawString(margin, y_position, line)
                y_position -= line_height

        pdf.save()
        
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import simpleSplit

class PDFgenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, title, sections):
        c = canvas.Canvas(self.filename, pagesize=letter)
        width, height = letter
        
        self.add_title(c, title, width, height)
        self.add_sections(c, sections, width, height)
        
        c.save()
    
    def add_title(self, c, title, width, height):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 50, title)
    
    def add_sections(self, c, sections, width, height):
        c.setFont("Helvetica", 12)
        y_position = height - 80
        
        for section_title, content in sections.items():
            # Add section title
            c.setFont("Helvetica-Bold", 14)
            c.drawString(100, y_position, section_title)
            y_position -= 20
            
            # Add section content
            c.setFont("Helvetica", 12)
            lines = simpleSplit(content, "Helvetica", 12, width - 150)
            for line in lines:
                c.drawString(100, y_position, line)
                y_position -= 15
                
                # If space is not enough, create a new page
                if y_position < 50:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = height - 50
